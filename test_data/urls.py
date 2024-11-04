from django.urls import path, include
from test_data import views


urlpatterns = [
    path('test_input/', views.TestInputView.as_view(), name= 'test_input'),
    path('<pk>/update', views.TestUpdateView.as_view(), name='update'), 
    path('update/<pk>', views.update_test_data, name='update_td'), 
    path('test_report_single/<int:pk>', views.TestReportSingle, name= 'test_report_single'),
    path('test_report_multi', views.TestReportMulti, name= 'test_report_multi'),
    path('test_report_multi_search', views.TestReportMultiSearch, name= 'test_report_multi_search'),
    path('report_search', views.report_search, name= 'report_search'),
    path('ajax/load-result/', views.ajax_load_result, name='ajax_load_result'),
    path('ajax/load-mfg/', views.ajax_load_mfg, name='ajax_load_mfg'),
    path('mfg_res_dropdown/', views.mfg_res_dropdown, name='mfg_res_dropdown'),
    path('register/', views.Register.as_view(), name='register'),
    path('three_phrase_inv/', views.ThreePhraseInv, name='three_phrase_inv'),
    path('about', views.about, name='about'),


    ]