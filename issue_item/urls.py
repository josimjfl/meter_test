from django.contrib import admin
from django.urls import path, include
from issue_item import views


urlpatterns = [
    path('issue_item', views.IssueItemView.as_view(), name= 'issue_item'),
    path('issue_seal', views.IssueSealView.as_view(), name= 'issue_seal'),
    path('issue_ajax', views.issue_ajax, name='issue_ajax'),
    path('update_issue_ajax', views.update_issue_ajax, name='update_issue_ajax'),
	path('meter_issue_list', views.meter_issue_list, name= 'meter_issue_list'),
	path('seal_issue_list', views.seal_issue_list, name= 'seal_issue_list'),
]