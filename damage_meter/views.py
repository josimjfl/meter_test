from django.shortcuts import render
from test_data.models import *
from balance_reg.models import Item
from accounts.models import CustomUser
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django import forms
from django.template import RequestContext
import django_excel as excel
from django.db.models import Count
from django.contrib.auth.decorators import login_required


@login_required
def DamageMeter(request):
    profile = CustomUser.objects.filter(office=request.user.office).latest('id')
    office = Office.objects.filter(id=profile.office.id).latest('id')
    test_data = Test_Data.objects.filter(remark="ব্যবহার অনুপযোগী।", office= request.user.office).order_by('id') #to get oposite data filter with ~Q(remark ='ব্যবহার উপযোগী।')
    paginator = Paginator(test_data, 24) # Show 24 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    date = datetime.date.today().strftime("%d-%m-%Y")

    return render(request, 'damage_meter/damage_meter.html',
        {'test_data':test_data, 'page_obj': page_obj, 'office':office, 'profile':profile, 'date':date})


@login_required
class UploadFileForm(forms.Form):
    file = forms.FileField()


@login_required
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html',
                              {'form': form})


@login_required
def download(request):
    if request.method == 'GET':
    	test_data = Test_Data.objects.filter(office=request.user.office, remark="ব্যবহার অনুপযোগী।").values_list('manufacturer', 'purchase_order', 'tested_meter_no', 'created_date', 'comments',  'book', 'account')
    	#print(test_data)
    	sheet = excel.pe.Sheet( test_data )
    	#sheet = excel.pe.Sheet([[1, 2, 10],[3, 4]])
    	return excel.make_response(sheet, "xlsx", file_name="All_damage_meter")  #csv, xls etc. can give.

    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        test_data = Test_Data.objects.filter(office=request.user.office, remark="ব্যবহার অনুপযোগী।", created_date__range=[from_date,to_date]).values_list('manufacturer', 'purchase_order', 'tested_meter_no', 'created_date', 'comments',  'book', 'account')
        
        sheet = excel.pe.Sheet( test_data )
        #sheet = excel.pe.Sheet([[1, 2, 10],[3, 4]])

        #make a file name line
        file_name = 'Damage_Meter_From_'+ str(from_date) +'_to_'+ str(to_date)

        return excel.make_response(sheet, "xlsx", file_name=file_name)  #csv, xls, xlsx etc. can give.
    

@login_required
def damage_report(request):
    from datetime import date

    # Default values for the form fields
    f_date = t_date = date.today().strftime('%d-%m-%Y')  # Default to today's date in the desired format

    if request.method == 'POST':
        f_date = request.POST.get('fromdate', f_date)
        t_date = request.POST.get('todate', t_date)

        # Convert dates to YYYY-MM-DD format for database queries
        from datetime import datetime
        fromdate = datetime.strptime(f_date, '%d-%m-%Y').date()
        todate = datetime.strptime(t_date, '%d-%m-%Y').date()

        # Prepare the data
        all_data = []
        manufacturers = Manufacturer.objects.all()
        total_sum_of_test_data_count = 0

        for manufacturer in manufacturers:
            test_data = Test_Data.objects.filter(
                office=request.user.office,
                manufacturer=manufacturer.name,
                remark="ব্যবহার অনুপযোগী।",
                created_date__range=[fromdate, todate]
            ).values('comments', 'meter_item').order_by('-meter_item')

            unique_comments = {item['comments'] for item in test_data if item['comments']}
            total_count = test_data.count()
            total_sum_of_test_data_count += total_count

            all_data.append({
                'manufacturer': manufacturer.name,
                'item': manufacturer.item_no,
                'cause': ' '.join(unique_comments),
                'total_count': total_count,
            })

        return render(request, 'damage_meter/damage_report.html', {
            'all_data': all_data,
            'total_sum_of_test_data_count': total_sum_of_test_data_count,
            'f_date': f_date,  # Pass user input back to the template
            't_date': t_date,  # Pass user input back to the template
        })

    return render(request, 'damage_meter/damage_report.html', {
        'f_date': f_date,
        't_date': t_date,
    })
