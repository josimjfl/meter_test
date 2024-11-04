from django.contrib import admin
from .models import *

# For Sort Item
from adminsortable2.admin import SortableAdminMixin

@admin.register(Results)
class ResultsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'get_items', 'details', 'order']


@admin.register(Manufacturer)
class ManufacturerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'item_no', 'order']


@admin.register(Test_Data)
class Test_dataAdmin(admin.ModelAdmin):
    list_display = ['id', 'tested_meter_no', 'meter_item', 'book', 'account', 'comments', 'created_date']
    search_fields = ['tested_meter_no']
    list_filter = ['meter_item', 'manufacturer']




