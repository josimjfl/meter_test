from django.contrib import admin

from .models import *

admin.site.register(CustomUser)
admin.site.register(Pbs)
admin.site.register(Standard_Meter)
admin.site.register(Office)
admin.site.register(Designation)
admin.site.register(OfficeEmp)