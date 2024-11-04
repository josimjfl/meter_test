from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from accounts.models import CustomUser



def add_employee(request):
	if request.method=="GET":
		emp = CustomUser.objects.filter(office=request.user.office)
		zonal_code = "09"
		return render(request, 'employee/add_employee.html', {'emp':emp, 'zonal_code':zonal_code})
"""
	if request.method=="POST":
		emp = Employee()
		name = request.POST.get('name')
		designation = request.POST.get('designation')
		breb_id = request.POST.get('breb_id')
		remark = request.POST.get('remark')
		zonal = request.POST.get('zonal_code')
		#for forigen key get id
		zonal_code = Sub_office.objects.get(id=zonal)
		pbs_code = zonal_code.pbs

		#save data to Employee Model
		emp.name = name
		emp.designation = designation
		emp.employee_id = breb_id
		emp.pbs_code = pbs_code
		emp.zonal_code = zonal_code
		emp.remark = remark
		emp.save()

		return redirect('add_employee')
"""