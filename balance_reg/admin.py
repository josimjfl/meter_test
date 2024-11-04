from django.contrib import admin
from .models import Item, SealBalance, Balance

# Register Item and SealBalance models
admin.site.register(Item)


# Customize the admin for Balance model
@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    # Display 'id' and 'item_no' from related 'Item' model
    list_display = ('id', 'item_item_no', 'date_start', 'sl_start', 'sl_end', 'store_return_ticket', 'ticket_no', 'referance_name', 'credit_qty', 'debit_qty')
    # Enable filtering based on 'item_no' from related 'Item' model
    list_filter = ('item__item_no', 'date_start',)
    

    # Optionally define how related 'item_item_no' is displayed
    def item_item_no(self, obj):
        return obj.item.item_no
    item_item_no.admin_order_field = 'item__item_no'  # Allow ordering by 'item_no'
    item_item_no.short_description = 'Item Number'    # Optional: Set display name



@admin.register(SealBalance)
class SealBalanceAdmin(admin.ModelAdmin):
    # Display 'id' and 'item_no' from related 'Item' model
    list_display = ('id', 'item', 'date_start', 'sl_start', 'sl_end', 'store_return_ticket', 'ticket_no', 'referance_name', 'credit_qty', 'debit_qty')
    # Enable filtering based on 'item' from related 'Item' model
    list_filter = ('item', 'date_start',)
    
