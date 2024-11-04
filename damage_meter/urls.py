from django.contrib import admin
from django.urls import path
from damage_meter.views import DamageMeter, download, upload


urlpatterns = [
    path('damage_meter/', DamageMeter, name='damage_meter'),
    path('download/', download, name='download'),
    path('upload/', upload, name='upload'),    
]