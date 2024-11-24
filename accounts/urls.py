
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # Custom
    #path('login/', custom_login_view, name='login'),  # Use this if you want a custom login view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Use this if you prefer Django's default login view
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile_update/', profile_update, name='profile_update'),
    path('<pk>/profile_update', update_user, name='profile_update'),

    # Password Reset URLs
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Password Change URLs (For logged-in users)
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    # For office Emp, office setups
    path('accounts/', office_emp_list, name='office_emp_list'),
    path('accounts/create/', office_emp_create, name='office_emp_create'),
    path('accounts/update/<int:pk>', office_emp_update, name='office_emp_update'),
    path('accounts/delete/<int:pk>/', office_emp_delete, name='office_emp_delete'),

    # Standard Meter Settings
    path('meters/', standard_meter_list, name='standard_meter_list'),
    path('meters/create/', standard_meter_create, name='standard_meter_create'),
    path('meters/update/<int:pk>/', standard_meter_update, name='standard_meter_update'),
    path('meters/delete/<int:pk>/', standard_meter_delete, name='standard_meter_delete'),
]
