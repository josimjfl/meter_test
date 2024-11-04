from django.shortcuts import render
from test_data.models import *
from accounts.models import CustomUser
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


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




from django.http import HttpResponseBadRequest
from django import forms
from django.template import RequestContext
import django_excel as excel

class UploadFileForm(forms.Form):
    file = forms.FileField()

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



def download(request):
    if request.method == 'GET':
    	test_data = Test_Data.objects.filter(remark="ব্যবহার অনুপযোগী।").values_list('manufacturer', 'purchase_order', 'tested_meter_no', 'created_date', 'comments',  'book', 'account')
    	#print(test_data)
    	sheet = excel.pe.Sheet( test_data )
    	#sheet = excel.pe.Sheet([[1, 2, 10],[3, 4]])
    	return excel.make_response(sheet, "xlsx", file_name="All_damage_meter")  #csv, xls etc. can give.

    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        test_data = Test_Data.objects.filter(remark="ব্যবহার অনুপযোগী।", created_date__range=[from_date,to_date]).values_list('manufacturer', 'purchase_order', 'tested_meter_no', 'created_date', 'comments',  'book', 'account')
        
        sheet = excel.pe.Sheet( test_data )
        #sheet = excel.pe.Sheet([[1, 2, 10],[3, 4]])

        #make a file name line
        file_name = 'Damage_Meter_From_'+ str(from_date) +'_to_'+ str(to_date)

        return excel.make_response(sheet, "xlsx", file_name=file_name)  #csv, xls, xlsx etc. can give.