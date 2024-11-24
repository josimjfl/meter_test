from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from django.utils.decorators import method_decorator  #for class based view
from django.urls import reverse
from django.views.generic.edit import UpdateView
from accounts.forms import CustomLoginForm, CustomUserForm
from .forms import UserUpdateForm
from .models import OfficeEmp, Office, CustomUser, Standard_Meter
from .forms import OfficeEmpForm
from .forms import StandardMeterForm


#make CutomUser to User
from django.contrib.auth import get_user_model
User = get_user_model()



def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect_user_based_on_role(user)
            else:
                form.add_error(None, 'আপনার ইউজারনেইম অথবা পাসওয়ার্ড সঠিক নয়!')  # Custom error message
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



def redirect_user_based_on_role(user):
	user_role = user.role
	if user_role == 'admin':
		return redirect('admin_dashboard')
	elif user_role == 'MT':
		return redirect('mt_dashboard')
	elif user_role == 'MTS':
		return redirect('mts_dashboard')
	elif user_role == 'IT':
		return redirect('it_dashboard')
	elif user_role == 'AGM':
		return redirect('agm_dashboard')
	elif user_role == 'DGM':
		return redirect('dgm_dashboard')
	elif user_role == 'BS':
		return redirect('bs_dashboard')
	elif user_role == 'JE':
		return redirect('je_dashboard')
	elif user_role == 'LT':
		return redirect('lt_dashboard')		
	else:
		return redirect('user_dashboard')



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@role_required(['admin', 'IT'])          #For user Group test  
def signup_view(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			username = request.POST['username']
			try:
				user = User.objects.get(username=username)
				return render(request, 'accounts/signup.html', {'error':'Username has already been taken.'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				#auth.login(request,user)
				return redirect('profile_update', user.id)
		else: 
			return render(request, 'accounts/signup.html', {'error':'password must match.'})
	else:
		return render(request, 'accounts/signup.html')




def profile(request):
	try:
		profile = CustomUser.objects.get(username=request.user)
		context = {'profile':profile}
	except CustomUser.DoesNotExist:
		context = {'profile': request.user }

	return render(request, 'accounts/profile.html', context)



@login_required
@role_required(['admin', 'IT'])          #For user Group test  
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        #profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid():
            user_form.save()
            return redirect('profile')  # Ensure this matches your URL name for profile detail view

    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form
    }

    return render(request, 'accounts/profile_update.html', context)		



@login_required
def admin_dashboard_view(request):
    return render(request, 'dashboard/admin_dashboard.html')



def update_user(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request=request, instance=user)
        if form.is_valid():
            form.save()
            return redirect('add_employee')
    else:
        form = CustomUserForm(instance=user, request=request)
    return render(request, 'accounts/custom_user.html', {'form': form})




# For Office Setup
@login_required
@role_required(['admin', 'IT'])          #For user Group test  
def office_emp_list(request):
    """List all OfficeEmp records."""
    if  request.user.role == 'IT':
        office_emps = OfficeEmp.objects.filter(office__pbs=request.user.office.pbs)
    else:
        office_emps = OfficeEmp.objects.filter(office=request.user.office)
    return render(request, 'accounts/office_emp_list.html', {'office_emps': office_emps})


@login_required
@role_required(['admin', 'IT'])          #For user Group test  
def office_emp_create(request):
    if request.method == 'POST':
        form = OfficeEmpForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('office_emp_list')
    else:
        form = OfficeEmpForm(user=request.user)
    return render(request, 'accounts/office_emp_form.html', {'form': form, 'action': 'Create'})




@login_required
@role_required(['admin', 'IT', 'MT', 'MTS'])          #For user Group test  
def office_emp_update(request, pk): 
    instance = get_object_or_404(OfficeEmp, pk=pk)
    if request.method == 'POST':
        form = OfficeEmpForm(request.POST, instance=instance, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('office_emp_list')
    else:
        form = OfficeEmpForm(instance=instance, user=request.user)
    return render(request, 'accounts/office_emp_form.html', {'form': form, 'action': 'Update'})



@login_required
@role_required(['admin', 'IT'])          #For user Group test  
def office_emp_delete(request, pk):
    """Delete an OfficeEmp record."""
    office_emp = get_object_or_404(OfficeEmp, pk=pk)
    if request.method == 'POST':
        office_emp.delete()
        return redirect('office_emp_list')
    return render(request, 'accounts/office_emp_confirm_delete.html', {'office_emp': office_emp})




# Standard meter settings
@login_required
@role_required(['admin', 'IT', 'MT', 'MTS'])          #For user Group test  
def standard_meter_list(request):
    # Filter Standard_Meter by the user's office
    meters = Standard_Meter.objects.filter(office=request.user.office)
    return render(request, 'accounts/standard_meter_list.html', {'meters': meters})




@login_required
@role_required(['admin', 'IT', 'MT', 'MTS'])          #For user Group test  
def standard_meter_create(request):
    if request.method == 'POST':
        form = StandardMeterForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('standard_meter_list')
    else:
        form = StandardMeterForm(user=request.user)
    return render(request, 'accounts/standard_meter_form.html', {'form': form, 'action': 'Add'})





@login_required
@role_required(['admin', 'IT', 'MT', 'MTS'])          #For user Group test  
def standard_meter_update(request, pk):
    meter = get_object_or_404(Standard_Meter, pk=pk)
    if request.method == 'POST':
        form = StandardMeterForm(request.POST, instance=meter, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('standard_meter_list')
    else:
        form = StandardMeterForm(instance=meter, user=request.user)
    return render(request, 'accounts/standard_meter_form.html', {'form': form, 'action': 'Update'})




@login_required
@role_required(['admin', 'IT', 'MT', 'MTS'])          #For user Group test  
def standard_meter_delete(request, pk):
    meter = get_object_or_404(Standard_Meter, pk=pk)
    if request.method == 'POST':
        meter.delete()
        return redirect('standard_meter_list')
    return render(request, 'accounts/standard_meter_confirm_delete.html', {'meter': meter})
