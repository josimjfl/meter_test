
from django.contrib import admin
from django.urls import path, include
from test_data import views
from balance_reg import urls
from django.conf.urls.static import static
from django.conf import settings 

#from django.conf.urls import url
 
urlpatterns = [
    path('', include('test_data.urls')),
    path('', include('accounts.urls')),
    path('', include('balance_reg.urls')),
    path('', include('meter_memo.urls')),
    path('', include('damage_meter.urls')),
    path('', include('dashboard.urls')),
    path('', include('issue_item.urls')),
    path('', include('employee.urls')),
    path('admin/', admin.site.urls),
    path('', views.Home, name= 'home'),



    path('page.html', views.upload, name='upload'),
    path('ajax/uploads/', views.uploadData, name='uploadData'),
    #url(r'^ajax/uploads/$', views.uploadData, name='uploadData'),
]

if settings.DEBUG:  # for image field
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





#To remove of off side navbar of django Admin
from django.contrib import admin
admin.autodiscover()
admin.site.enable_nav_sidebar = False


#404 and 500 custom page handler
handler404 = 'meter_test.views.handler404' #Not found
handler500 = 'meter_test.views.handler500' #Server problem
handler400 = 'meter_test.views.handler400' #Bed 

#403 page handeler
from django.conf.urls import handler403
from .views import custom_permission_denied_view

handler403 = custom_permission_denied_view