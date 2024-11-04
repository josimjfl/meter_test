from django.contrib import admin
from django.urls import path, include
from meter_memo import views


urlpatterns = [
    path('meter_memo', views.MeterMemo, name='meter_memo'),
]