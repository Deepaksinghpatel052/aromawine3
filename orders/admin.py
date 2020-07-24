from django.contrib import admin
from .models import AwOrders,AwAddToCard,AwOrederItem,AwOrderNote
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwOrdersAdmin(ImportExportModelAdmin):
    list_display = ('User','order_id', 'Order_address', 'Order_Type','Quentity','Amount','Payment_Status','Payment_Method','Order_Date','delivery_Date','Payment_Date')
admin.site.register(AwOrders,AwOrdersAdmin)

class AwAddToCardAdmin(ImportExportModelAdmin):
    list_display = ('User','Product', 'Year', 'Type','Case_Formate','Quentity','Date')
    list_filter = ('User','Product','Date','Year',)
admin.site.register(AwAddToCard,AwAddToCardAdmin)


class AwOrederItemAdmin(ImportExportModelAdmin):
    list_display = ('User','Order_id', 'Product', 'Year','Type','Case_Formate','Cost_of_product','Quentity','Total_cost')
admin.site.register(AwOrederItem,AwOrederItemAdmin)

class AwOrderNoteAdmin(ImportExportModelAdmin):
    list_display = ('User','Order_id', 'Display_Status','Note','Attachment', 'Date')
admin.site.register(AwOrderNote,AwOrderNoteAdmin)