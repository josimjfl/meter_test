from django.contrib import admin
from django.urls import path, include
from balance_reg import views


urlpatterns = [
    path('balance', views.BalanceView.as_view(), name= 'balance'),
    path('issue_item_to_bl/', views.IssueItem.as_view(), name= 'issue_item_to_bl'),
    path('receive_item', views.AddItem.as_view(), name='receive_item'),
    path('balance_summary', views.balance_summary_view, name='balance_summary'),
    path('item_list', views.item_list, name='item_list'),
    path('update-item-order/', views.update_item_order, name='update_item_order'),
    path('last_balance/', views.last_balance, name='last_balance'),
]