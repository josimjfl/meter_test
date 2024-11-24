from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from accounts.models import CustomUser



def add_employee(request):
    if request.method == "GET":
        # Filter employees based on the user's role
        if request.user.role == 'IT':
            emp = CustomUser.objects.filter(office__pbs=request.user.office.pbs)
        else:
            emp = CustomUser.objects.filter(office=request.user.office)

        # Render the employee list to the template
        return render(request, 'employee/add_employee.html', {'emp': emp})

