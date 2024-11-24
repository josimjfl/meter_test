from django.shortcuts import render
from test_data.models import *
from accounts.models import CustomUser, Standard_Meter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required
def MeterMemo(request):
    profile = CustomUser.objects.filter(office=request.user.office).latest('id')
    office = Office.objects.get(id=request.user.office.id)
    test_data = Test_Data.objects.filter(office= request.user.office).order_by('id')
    paginator = Paginator(test_data, 24) # Show 24 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    date = datetime.date.today().strftime("%d-%m-%Y")

    return render(request, 'meter_memo/meter_memo_multi.html',
        {'test_data':test_data, 'page_obj': page_obj, 'office':office, 'profile':profile, 'date':date})