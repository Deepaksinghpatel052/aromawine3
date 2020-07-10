from django.contrib import admin
from .models import AwOrders,AwAddToCard
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwOrdersAdmin(ImportExportModelAdmin):
    list_display = ('User','order_id', 'Order_address', 'Order_Type','Quentity','Amount','Payment_Status','Payment_Method','Order_Date','delivery_Date','Payment_Date')
admin.site.register(AwOrders,AwOrdersAdmin)

class AwAddToCardAdmin(ImportExportModelAdmin):
    list_display = ('User','Product', 'Year', 'Type','Case_Formate','Quentity','Date')
    list_filter = ('User','Product','Date','Year',)
admin.site.register(AwAddToCard,AwAddToCardAdmin)
