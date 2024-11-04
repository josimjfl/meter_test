from django.contrib import admin
from django.urls import path, include
from dashboard import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('mt_dashboard', views.mt_dashboard, name='mt_dashboard'),
    path('mts_dashboard', views.mts_dashboard, name='mts_dashboard'),
    path('agm_dashboard', views.agm_dashboard, name='agm_dashboard'),
    path('bs_dashboard', views.bs_dashboard, name='bs_dashboard'),
    path('je_dashboard', views.lm_dashboard, name='je_dashboard'),
    path('lt_dashboard', views.lm_dashboard, name='lt_dashboard'),
    path('lm_dashboard', views.lm_dashboard, name='lm_dashboard'),
    path('it_dashboard', views.it_dashboard, name='it_dashboard'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
]