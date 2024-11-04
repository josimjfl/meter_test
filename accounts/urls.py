# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile_update/', profile_update, name='profile_update'),
    path('<pk>/profile_update', ProfileUpdate.as_view(), name='profile_update'),
]