import datetime
today=datetime.date.today().strftime("%d-%m-%Y")
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
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from datetime import datetime
from django.db.models import Q




@login_required
@role_required(['admin', 'IT', 'MT', 'MTS'])          #For user Group test  
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



@login_required
def upload(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'test_data/page.html', {})



@login_required
def Home(request):
    test_complete = Test_Data.objects.count()  # Total test data count
    role = request.user.role  # Current user's role
    pending = 0  # Default pending count
    last_pending = None  # Default last pending entry

    # Filter test data based on the user's role
    if role in ['MTS', 'MT']:
        test_data_queryset = Test_Data.objects.filter(
            office=request.user.office,
            checked_by__isnull=True
        )
    elif role in ['AGM', 'DGM']:
        test_data_queryset = Test_Data.objects.filter(
            office=request.user.office,
            counter_sign_by__isnull=True,
            checked_by__isnull=False
        )
    elif role in ['BS', 'BA']:
        test_data_queryset = Test_Data.objects.filter(
            office=request.user.office,
            received_by__isnull=True,
            counter_sign_by__isnull=False,
            checked_by__isnull=False
        )
    else:
        test_data_queryset = Test_Data.objects.none()  # Empty queryset for roles without specific rules

    # Calculate pending count and get the latest entry if the queryset exists
    pending = test_data_queryset.count()
    last_pending = test_data_queryset.values(
        'id', 'tested_meter_no', 'reading_as_found', 'book', 'account', 'comments', 'created_date'
    ).latest('id') if test_data_queryset.exists() else None

    # Render the template with context data
    return render(request, 'test_data/home.html', {
        'last_pending': last_pending,
        'pending': pending,
        'test_complete': test_complete,
        'role': role,
    })



    

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
        mfg = Manufacturer.objects.all()
        result = Results.objects.all()
        item_no = Item.objects.all()
        date = today
        try:            
            test_data = Test_Data.objects.filter(office= self.request.user.office).latest('id')
        except:
            return render(self.request,'test_data/test_input.html', {'mfg':mfg, 'results':result, 'date':date, 'item_no':item_no, 'results':result, 'msg':"Welcome to Josim Uddin MT"})

        po = PurchaseOrder.objects.all()
        total_td= len(Test_Data.objects.all())
        pg=str(round(total_td//12))
        idpg=str(total_td %12)
        context ={
            'mfg':mfg,
            'item_no':item_no,
            'results':result, 
            'date':date,
            'test_data':test_data, 
            "pg":pg, 'po':po,
            "idpg":idpg, 
            'msg':"Welcome to Josim Uddin MT"
            }

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
                td.created_date=datetime.now()
                td.updated_date=datetime.now()
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
    return JsonResponse({'id':mfg.id, 
        'item_no': mfg.item_no.item_no, 
        'kh':mfg.kh, 
        'name':mfg.name, 
        'meter_class':mfg.meter_class, 
        'LL_TA':mfg.LL_TA, 
        'FL_TA':mfg.FL_TA, 
        'LL_rev':mfg.LL_rev, 
        'FL_rev':mfg.FL_rev, 
        'standerd_rev_req_ll':mfg.standerd_rev_req_ll,
        'standerd_rev_req_fl':mfg.standerd_rev_req_fl
        }, safe=False)         



@login_required
def  test_report_list(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))  # Get the requested page number or default to 1

        # Filter the queryset
        posts = Test_Data.objects.filter(
            office=request.user.office,
            counter_sign_by__isnull=False,
            checked_by__isnull=False
        ).order_by('-id')

        # Pagination setup
        content_per_page = 5
        paginator_obj = Paginator(posts, content_per_page)

        try:
            post_page = paginator_obj.page(page)
        except EmptyPage:
            post_page = paginator_obj.page(paginator_obj.num_pages)  # Return the last page if out of range

        # Check if the request is an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Serialize data for JSON response
            serialized_data = [
                {
                    "id": obj.id,
                    "meter_no": obj.tested_meter_no,
                    "reading": obj.reading_as_found,
                    "book" : obj.book,
                    "account": obj.account,
                    "result": obj.comments,
                    "print_counter": obj.print_counter,
                    "date": obj.counter_sign_date.strftime('%Y-%m-%d') if obj.counter_sign_date else None,
                }
                for obj in post_page
            ]
            return JsonResponse({
                "content": serialized_data,
                "total_pages": paginator_obj.num_pages,
            })

        # Render the full page for non-AJAX requests
        context = {
            "posts": post_page,
        }
        return render(request, 'test_data/test_report_list.html', context)



@login_required
def TestReportSingle(request, pk=None):
    # Fetch user's office and user
    office = Office.objects.get(id=request.user.office.id)
    user = request.user

    # Process GET request
    if request.method == 'GET':
        book = request.GET.get('book')
        account = request.GET.get('account')

        # Retrieve Test_Data
        if pk is not None:
            data = get_object_or_404(Test_Data, pk=pk, office=office)
        elif book and account:
            data = get_object_or_404(Test_Data, book=book, account=account, office=office)
        else:
            return render(request, 'test_data/test_report_single_input.html')

        # Update data if user has required role
        if user.role in ['BS', 'BA']:
            Test_Data.objects.filter(pk=data.id).update(
                received_by=user.id,
                received_date=datetime.now(),
                print_counter=data.print_counter + 1
            )

        return render(request, 'test_data/test_report_single.html', {'office': office, 'data': data})

    # Process POST request
    elif request.method == 'POST':
        test_id = request.POST.get('test_id')
        book = request.POST.get('book')
        account = request.POST.get('account')

        # Retrieve Test_Data
        if test_id:
            data = get_object_or_404(Test_Data, pk=test_id, office=office)
        elif book and account:
            data = get_object_or_404(Test_Data, book=book, account=account, office=office)
        else:
            return render(request, 'test_data/test_report_single_input.html')

        # Update data if user has required role
        if user.role in ['BS', 'BA']:
            Test_Data.objects.filter(pk=data.id).update(
                received_by=user.id,
                received_date=datetime.now(),
                print_counter=data.print_counter + 1
            )

        return render(request, 'test_data/test_report_single.html', {'office': office, 'data': data})




@login_required(login_url="login")
@role_required(['admin', 'IT', 'MT', 'MTS', 'AGM', 'DGM'])          #For user Group test
def TestReportMulti(request):
    office = Office.objects.get(id=request.user.office.id)

    test_data = Test_Data.objects.filter(office=request.user.office)

    # Pagination
    paginator = Paginator(test_data, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'test_data/test_report_multi.html', {
        'test_data': test_data, 
        'page_obj': page_obj, 
        'office': office
    })




def TestReportMultiSearch(request):
    try:
        latest_test = Test_Data.objects.filter(office= request.user.office).latest('id')
    except Test_Data.DoesNotExist:
        latest_test = None
    return render(request, 'test_data/test_report_multi_search.html', {"latest_test":latest_test})



from datetime import datetime

@login_required
def report_search(request):
    if request.method == "GET":
        search_option = request.GET.get('search_option')
        search_value = request.GET.get('search_value')
        book = request.GET.get('book')
        account = request.GET.get('account')
        f_date = request.GET.get('fromdate')
        t_date = request.GET.get('todate')
        fromid = request.GET.get('fromid')
        toid = request.GET.get('toid')

        # Initialize an empty queryset
        test_data = Test_Data.objects.none()

        # Filtering logic
        if search_option and search_value:
            variable_column = search_option
            search_type = 'icontains'
            filt = f"{variable_column}__{search_type}"
            test_data = Test_Data.objects.filter(
                office=request.user.office, **{filt: search_value}
            )
        elif book and account:
            test_data = Test_Data.objects.filter(
                office=request.user.office, book=book, account=account
            )
        elif f_date and t_date:
            try:
                fromdate = datetime.strptime(f_date, '%d-%m-%Y').date()
                todate = datetime.strptime(t_date, '%d-%m-%Y').date()
                test_data = Test_Data.objects.filter(
                    office=request.user.office, created_date__range=[fromdate, todate]
                )
            except ValueError:
                pass
        elif fromid and toid:
            test_data = Test_Data.objects.filter(
                office=request.user.office, id__range=[fromid, toid]
            )

        # Count rows
        count_pay = test_data.count()

        # Office standard meter
        office = OfficeEmp.objects.get(office=request.user.office)
        std = office.standered_meter

        # Pagination
        paginator = Paginator(test_data, 12)  # 12 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Preserve query parameters
        query_params = request.GET.copy()
        query_params.pop('page', None)  # Exclude 'page' parameter
        query_string = query_params.urlencode()

        return render(request, 'test_data/test_report_multi.html', {
            'test_data': page_obj.object_list,
            'page_obj': page_obj,
            'std': std,
            'count_pay': count_pay,
            'query_string': query_string,
        })



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




from datetime import datetime

@login_required
def ThreePhraseInv(request):
    if request.method == "GET":
        f_date = request.GET.get('fromdate')
        t_date = request.GET.get('todate')
        fromid = request.GET.get('fromid')
        toid = request.GET.get('toid')

        # Initialize an empty queryset
        test_data = Test_Data.objects.none()

        # Debugging: Check the received GET parameters
        print(f"fromdate: {f_date}, todate: {t_date}, fromid: {fromid}, toid: {toid}")

        # Filtering logic
        if f_date and t_date:
            try:
                # Convert string dates to datetime objects
                fromdate = datetime.strptime(f_date, '%d-%m-%Y').date()
                todate = datetime.strptime(t_date, '%d-%m-%Y').date()

                test_data = Test_Data.objects.filter(
                    office=request.user.office, created_date__range=[fromdate, todate]
                )
            except ValueError:
                print("Invalid date format.")
        elif fromid and toid:
            test_data = Test_Data.objects.filter(
                office=request.user.office, id__range=[fromid, toid]
            )

        else:
            print("No filter provided.")
            return render(request, 'test_data/three_phrase_inv_search.html')

        # Count the number of records found
        count_pay = test_data.count()

        # Get office standard meter
        officeE = OfficeEmp.objects.get(office=request.user.office)
        std = officeE.standered_meter

        office = Office.objects.get(id=request.user.office.id)

        # Pagination logic
        paginator = Paginator(test_data, 12)  # 12 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Preserve other query parameters except for 'page'
        query_params = request.GET.copy()
        query_params.pop('page', None)  # Remove the 'page' parameter
        query_string = query_params.urlencode()  # Create query string

        return render(request, 'test_data/three_phrase_inv.html', {
            'test_data': page_obj.object_list,
            'page_obj': page_obj,
            'std': std,
            'count_pay': count_pay,
            'query_string': query_string,
            'office': office,
        })




@method_decorator(role_required(['MT', 'MTS', 'admin']), name='dispatch')
class TestUpdateView(UpdateView):
    model = Test_Data
    #fields = '__all__'
    form_class = TestDataUpdateForm
    template_name = 'test_data/test_update.html'
    success_url ="/test_report_multi"




@csrf_exempt
@login_required
@role_required(['admin', 'MT', 'MTS'])          #For user Group test
def update_test_data(request, pk):
    td = get_object_or_404(Test_Data, pk=pk, office= request.user.office)
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




# All right reserved by josimmsc@gmail.com as Josim Uddin