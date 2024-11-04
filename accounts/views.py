from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from django.utils.decorators import method_decorator  #for class based view
from django.urls import reverse
from .models import CustomUser
from django.views.generic.edit import UpdateView
from accounts.forms import CustomLoginForm, CustomUserForm
from django.http import JsonResponse
from .forms import UserUpdateForm
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
        print(f"User: {request.user}")
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form
    }

    return render(request, 'accounts/profile_update.html', context)		



@login_required
def admin_dashboard_view(request):
    return render(request, 'dashboard/admin_dashboard.html')


@method_decorator(role_required(['IT', 'admin']), name='dispatch')
class ProfileUpdate(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'test_data/custom_user.html'
    success_url = "/"
