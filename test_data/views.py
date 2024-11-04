import datetime
today=datetime.date.today().strftime("%Y-%m-%d")
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, View
from django.views.generic.edit import UpdateView
from .models import *
from accounts.models import CustomUser, Standard_Meter, OfficeEmp
from balance_reg.models import Item
from damage_meter.models import PurchaseOrder
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import TestDataUpdateForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from django.utils.decorators import method_decorator  #for class based view




def uploadData(request):
    res = {'error': True, 'msg': "Something went wrong."}
    allowed_files = ["csv", "xls", "xlsx", "xlsm", "xlsb"]
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        userid = request.POST['user_id']
        name = request.POST['fullname']
        email = request.POST['email']
        url = request.POST['url']
        file = ""
        refile = ""
        ErrorF = {'error': False, "msg": ""}
        if userid and name and email and url: 
            if not ErrorF['error']:
                u = uploads.objects.create(fullname=name, email=email, url=url)
                u.save()
                res = {'error': False, 'msg': "Successfully Submited."}
            elif ErrorF['error']:
                res = ErrorF
            else:
                res = {'error': True, 'msg': "Form not submitted. Try with a refresh."}
        else:
            res = {'error': True, 'msg': "Fill all required fields."}
        return JsonResponse(res, safe=False)


def upload(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'test_data/page.html', {})



def Home(request):
    return render(request, 'test_data/home.html', {})
    

def mfg_res_dropdown(request):
    item_no = request.GET.get('item_no')
    #filter manufacturer by item_no
    manufacture = Manufacturer.objects.filter(item_no__id=item_no)
    data_mfg = [{'id': mfg.id, 'name': mfg.name} for mfg in manufacture]

    #filter Result by item_no
    result = Results.objects.filter(items__id__icontains=item_no)
    data_res = [{'id': res.id, 'name': res.name} for res in result]

    #return data as json format for dropdown menu
    data = {'mfg': data_mfg,'res': data_res}
    return JsonResponse(data, safe=False)


@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')
class TestInputView(View):
    def get(self, *args, **kwargs):
        mfg = Manufacturer.objects.filter(item_no=Item.objects.get(item_no="J-39"))
        result = Results.objects.filter(items__item_no__icontains="J-39")
        item_no = Item.objects.all()
        date = today
        try:            
            test_data = Test_Data.objects.filter(office= self.request.user.office).latest('id')
        except:
            return render(self.request,'test_data/test_input.html', {'mfg':mfg, 'results':result, 'date':date})

        po = PurchaseOrder.objects.all()
        total_td= len(Test_Data.objects.all())
        pg=str(round(total_td//12))
        idpg=str(total_td %12)
        context ={
            'mfg':mfg, 'item_no':item_no,
            'results':result, 'date':date,
            'test_data':test_data, "pg":pg, 'po':po,
            "idpg":idpg, 'msg':"Welcome to Josim Uddin MT"}

        return render(self.request,'test_data/test_input.html', context)


    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            res = {'error': True, 'msg': "Something went wrong."}
            m =self.request.POST.get('tested_meter_no')
            td=Test_Data()
            td.office = self.request.user.office
            td.tested_meter_no=self.request.POST.get('tested_meter_no')
            reading = self.request.POST.get('reading_as_found')
            td.cmo = self.request.POST.get('cmo')
            td.book = self.request.POST.get('book')
            td.account = self.request.POST.get('account')

            mfg = self.request.POST.get('manufacturer')
            td.manufacturer = Manufacturer.objects.get(id=mfg)
            td.meter_class = self.request.POST.get('meter_class')
            td.meter_item = self.request.POST.get('meter_item')
            td.kh = self.request.POST.get('kh')
            td.LL_TA = self.request.POST.get('LL_TA')
            td.FL_TA = self.request.POST.get('FL_TA')
            td.LL_rev = self.request.POST.get('LL_rev')
            td.FL_rev = self.request.POST.get('FL_rev')
            td.standerd_rev_req_ll = self.request.POST.get('standerd_rev_req_ll')
            td.standerd_rev_req_fl = self.request.POST.get('standerd_rev_req_fl')

            if reading != "":                                   #To set all reading for not run
                td.reading_as_found = reading
                error_ll = self.request.POST.get('error_ll')
                if error_ll == "--":                     #To stop reading +0.1
                    td.reading_as_left = reading
                else:
                    td.reading_as_left = float(reading)+0.1
                td.error_ll = self.request.POST.get('error_ll')
                td.error_fl = self.request.POST.get('error_fl')
                td.as_found_ll = self.request.POST.get('as_found_ll') 
                td.as_found_fl = self.request.POST.get('as_found_fl')
                td.percent_found_ll = self.request.POST.get('percent_ll')
                td.percent_found_fl = self.request.POST.get('percent_fl')
                td.percent_left_ll = self.request.POST.get('percent_ll_left')
                td.percent_left_fl = self.request.POST.get('percent_fl_left')
                td.as_left_ll = self.request.POST.get('as_found_ll')
                td.as_left_fl = self.request.POST.get('as_found_fl')
                td.error_left_ll = self.request.POST.get('error_ll')
                td.error_left_fl = self.request.POST.get('error_fl')
            else:
                td.reading_as_found = "x"
                td.reading_as_left = "x"
                td.error_ll = "--"
                td.error_fl = "--"
                td.as_found_ll = "--"
                td.as_found_fl = "--"
                td.percent_found_ll = "--"
                td.percent_found_fl = "--"
                td.percent_left_ll = "--"
                td.percent_left_fl = "--"
                td.as_left_ll = "--"
                td.as_left_fl = "--"
                td.error_left_ll = "--"
                td.error_left_fl = "--"


            td.terminal_seal = self.request.POST.get('terminal_seal')
            td.body_seal = self.request.POST.get('body_seal')
            td.comments = self.request.POST.get('comments')
            td.remark = self.request.POST.get('remark')
            td.cmo_type = self.request.POST.get('cmo_type')
            td.date = self.request.POST.get('date')
            td.purchase_order = self.request.POST.get('purchase_order')
            td.created_by = self.request.user
            td.terminal_seal = self.request.POST.get('terminal_seal')
            td.terminal_seal_no = self.request.POST.get('terminal_seal_no')
            td.terminal_seal_missing = self.request.POST.get('terminal_seal_missing')
            td.body_seal = self.request.POST.get('body_seal')
            td.glass_cover = self.request.POST.get('glass_cover')
            td.test_clip = self.request.POST.get('test_clip')
            td.remove_cause = self.request.POST.get('remove_cause')
            remove_date = self.request.POST.get('remove_date')
            if remove_date != "":
                td.remove_date = remove_date

            #PurchaseOrder save
            if not PurchaseOrder.objects.filter(purchase_order = td.purchase_order).exists():
                purchase = PurchaseOrder()
                purchase.purchase_order = td.purchase_order
                purchase.save()

            #Duplicate not save    
            if Test_Data.objects.filter(office=self.request.user.office, tested_meter_no = td.tested_meter_no, book = td.book, account=td.account).exists():
                #messages.warning(self.request, 'Duplicate: পূর্বেই টেস্ট ডাটা করা হয়েছে')
                total_td= len(Test_Data.objects.all())
                pg=str(round(total_td//12))
                idpg=str(total_td %12)
                res = {'error': True, 'msg': "পূর্বেই টেস্ট ডাটা করা হয়েছে", 'tested_meter_no': td.tested_meter_no, 'last_id':td.id, 'pg':pg, 'idpg':idpg, 'last_reading':td.reading_as_found}
                return JsonResponse(res, safe=False)

            else:
                td.created_by= self.request.user
                td.updated_by= self.request.user
                td.created_date=datetime.datetime.now()
                td.updated_date=datetime.datetime.now()
                td.save()
                #messages.success(self.request, 'Test Successful')

                total_td= len(Test_Data.objects.all())
                pg=str(round(total_td//12))
                idpg=str(total_td %12)

                res = {'error': False, 'msg': "Successfully Submited", 'tested_meter_no': td.tested_meter_no, 'last_id':td.id, 'pg':pg, 'idpg':idpg, 'last_reading':td.reading_as_found, 'cmo':td.cmo}
                return JsonResponse(res, safe=False)
                #return redirect('/')


def ajax_load_result(request):
    result_id = request.GET.get('resultid')
    dist = Results.objects.filter(id=result_id)
    return JsonResponse(list(dist.values('remark', 'details', 'name')), safe=False)


def ajax_load_mfg(request):
    result_id = request.GET.get('mfgid')
    mfg = Manufacturer.objects.get(id=result_id)
    return JsonResponse({'id':mfg.id, 'item_no':mfg.item_no.item_no, 'kh':mfg.kh, 'name':mfg.name, 'meter_class':mfg.meter_class, 'LL_TA':mfg.LL_TA, 'FL_TA':mfg.FL_TA, 'LL_rev':mfg.LL_rev, 'FL_rev':mfg.FL_rev, 'standerd_rev_req_ll':mfg.standerd_rev_req_ll,
'standerd_rev_req_fl':mfg.standerd_rev_req_fl}, safe=False)         



def TestReportSingle(request, pk):
    office = Office.objects.get(id=request.user.office.id)
    user_id = request.user
    custom_user=''
    mts=''
    agm=''

    if request.method == 'GET':
        if pk != 0:
            data = get_object_or_404(Test_Data, pk=pk, office=request.user.office)

            return render(request, 'test_data/test_report_single.html', {'office':office, 'data':data})
        else:
            return render(request, 'test_data/test_report_single_input.html')


    if request.method=='POST':
        test_id = request.POST.get('test_id')
        book= request.POST.get('book')
        account = request.POST.get('account')
        if test_id != None:
            data = get_object_or_404(Test_Data, pk=test_id, office=request.user.office)

        elif book != None and account !=None:
            data = get_object_or_404(Test_Data, book=book, account=account)
            
        else:
            return render(request, 'test_data/test_report_single_input.html')

        return render(request, 'test_data/test_report_single.html', {'office':office, 'data':data})



@login_required(login_url="login")
def TestReportMulti(request):
    custom_user = CustomUser.objects.get(id=request.user.id)
    office = Office.objects.get(id=request.user.office.id)
    """except Exception as e:
        return render(request, 'test_data/no_permission.html')
    """
    test_data = Test_Data.objects.filter(office= request.user.office).order_by('id')

    paginator = Paginator(test_data, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    date = datetime.date.today().strftime("%d-%m-%Y")

    return render(request, 'test_data/test_report_multi.html',
        {'test_data':test_data, 'page_obj': page_obj, 'date':date, 'office':office})


def TestReportMultiSearch(request):
    try:
        latest_test = Test_Data.objects.filter(office= request.user.office).latest('id')
    except Test_Data.DoesNotExist:
        latest_test = None
    return render(request, 'test_data/test_report_multi_search.html', {"latest_test":latest_test})

def report_search(request):
    if request.method=="GET":
        search_option = request.GET.get('search_option')
        search_value = request.GET.get('search_value')
        book= request.GET.get('book')
        account= request.GET.get('account')
        if search_option != None:
            #for dynamic search
            variable_column = search_option
            search_type = 'icontains'
            filt = variable_column + '__' + search_type
            try:
                test_data = Test_Data.objects.filter(office=request.user.office, **{filt: search_value})
            except Test_Data.DoesNotExist:
                test_data = None
        elif book != None and account != None:
            book= request.GET.get('book')
            account= request.GET.get('account')
            test_data=Test_Data.objects.filter(office=request.user.office, book=book, account=account)
        else:
            fromdate = request.GET.get('fromdate')
            todate = request.GET.get('todate')
            if fromdate != None:
                try:
                    test_data = Test_Data.objects.filter(office=request.user.office, created_date__range=[fromdate,todate]).order_by('id')
                except Test_Data.DoesNotExist:
                    test_data = None
            else:
                fromid = request.GET.get('fromid')
                toid = request.GET.get('toid')
                test_data = Test_Data.objects.filter(office=request.user.office, id__range=[fromid,toid]).order_by('id')

        count_pay=len(test_data)      #to get sum of data row or quantity

        office = OfficeEmp.objects.get(office=request.user.office)
        std = office.standered_meter

        paginator = Paginator(test_data, 12) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'test_data/test_report_multi.html',
            {'test_data':test_data, 'page_obj': page_obj, 'std':std})

        """
        if 'list' in request.GET:
            return render(request, "pathology/lazer_report.html", context)
        elif 'search' in request.GET:
            return render(request, "test_data/test_report_multi_search.html", context)
        """
@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')
class Register(View):
    def get(self, *args, **kwargs):
        try:
            #get latest id to show in search
            last_id = Test_Data.objects.filter(office=self.request.user.office).latest('id')
        except:
            last_id = None

        return render(self.request, 'test_data/register_search.html', {'last_id': last_id.id})

    def post(self, *args, **kwargs):
        if self.request.method=="POST":
            fromid=self.request.POST.get('fromid')
            toid=self.request.POST.get('toid')
            change_cmo_data=Test_Data.objects.filter(office=self.request.user.office, id__range=[fromid,toid], cmo_type="Change").order_by('id')
            remove_cmo_data=Test_Data.objects.filter(office=self.request.user.office, id__range=[fromid,toid], cmo_type="Remove").order_by('id')


            change = [change_cmo_data[i:i+8] for i in range(0, len(change_cmo_data), 8)] # for table 8 column loop
            remove = [remove_cmo_data[i:i+8] for i in range(0, len(remove_cmo_data), 8)] # for table 8 column loop

            total_remove = len(remove_cmo_data)
            total_change = len(change_cmo_data)

            context = {
                'change':change,
                'remove':remove, 
                'total_change':total_change, 
                'total_remove': total_remove, 
                'fromid':fromid,
                'toid':toid
                }

            return render(self.request, 'test_data/register.html', context)



def about(request):
    return render(request, 'test_data/about.html')




@login_required(login_url="login")
def ThreePhraseInv(request):
    if request.method == "GET":
        try:
            latest_test = Test_Data.objects.filter(office= request.user.office).latest('id')
        except Test_Data.DoesNotExist:
            latest_test = None
        return render(request, 'test_data/three_phrase_inv_search.html', {"latest_test":latest_test})


    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        if fromdate != None and todate != None:
            try:
                test_data = Test_Data.objects.filter(office=request.user.office, remark="পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।", created_date__range=[fromdate,todate]).order_by('id')
            except Test_Data.DoesNotExist:
                test_data = None
        else:
            fromid = request.POST.get('fromid')
            toid = request.POST.get('toid')
            try:
                test_data = Test_Data.objects.filter(office=request.user.office, remark="পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।", id__range=[fromid,toid]).order_by('id')
            except Test_Data.DoesNotExist:
                test_data = None
            

        count_pay=len(test_data)      #to get sum of data row or quantity

        paginator = Paginator(test_data, 12) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'test_data/three_phrase_inv.html',{'test_data':test_data, 'page_obj': page_obj})





@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')
class TestUpdateView(UpdateView):
    model = Test_Data
    #fields = '__all__'
    form_class = TestDataUpdateForm
    template_name = 'test_data/test_update.html'
    success_url ="/test_report_multi"




from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def update_test_data(request, pk):
    td = get_object_or_404(Test_Data, pk=pk, office= request.user.office)
    print(td)


    mfg = Manufacturer.objects.filter(item_no=Item.objects.get(item_no="J-39"))
    result = Results.objects.filter(items__item_no__icontains="J-39")
    item_no = Item.objects.all()
    date = today
    try:            
        test_data = Test_Data.objects.filter(office= request.user.office).latest('id')
    except:
        return render(request,'test_data/test_input.html', {'mfg':mfg, 'results':result, 'date':date})

    po = PurchaseOrder.objects.all()
    total_td= len(Test_Data.objects.all())
    pg=str(round(total_td//12))
    idpg=str(total_td %12)

    
    if request.method == 'POST':
        form = TestDataUpdateForm(request.POST, instance=td)
        if form.is_valid():
            #To save mfg name in td, Retrieve the selected manufacturer ID
            selected_manufacturer_id = request.POST.get('manufacturer')
            reading_as_found = request.POST.get('reading_as_found')

            if selected_manufacturer_id:
                # Fetch the manufacturer object using the ID
                selected_manufacturer = Manufacturer.objects.get(pk=selected_manufacturer_id)
                # Save the manufacturer's name in the Test_Data model
                form.instance.manufacturer = selected_manufacturer.name

                #To save reading_as_left from as_found
                if reading_as_found:
                    reading_found = float(reading_as_found)
                    if reading_found >= 0:
                        form.instance.reading_as_left = reading_found + 0.1
                    else:
                        form.instance.reading_as_left = 'x'
                        form.instance.reading_as_found = 'x'
                else:
                    form.instance.reading_as_left = 'x'
                    form.instance.reading_as_found = 'x'

            form.save()

            response_data = {
                'success': True,
                'message': 'Test data updated successfully!'
            }
        else:
            response_data = {
                'success': False,
                'errors': form.errors.as_json(),
            }
        return JsonResponse(response_data)

    form = TestDataUpdateForm(instance=td)
    test_data_id = form.instance.id

    context = {
        #update
        'form': form,
        'test_data': test_data,
        'test_data_id': test_data_id,
        #regular
        'mfg':mfg, 'item_no':item_no,
        'results':result, 'date':date,
        "pg":pg, 'po':po,
        "idpg":idpg, 'msg':"Welcome to Josim Uddin MT"
    }
    return render(request, 'test_data/test_input_edit.html', context)
