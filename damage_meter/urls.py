from django.contrib import admin
from django.urls import path
from damage_meter.views import DamageMeter, download, upload, damage_report


urlpatterns = [
    path('damage_meter/', DamageMeter, name='damage_meter'),
    path('download/', download, name='download'),
    path('upload/', upload, name='upload'),
    path('damage_report/', damage_report, name='damage_report'),
]