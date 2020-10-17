from django.contrib import admin
from .models import AwOrders,AwAddToCard,AwOrederItem,AwOrderNote
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwOrdersAdmin(ImportExportModelAdmin):
    list_display = ('User','order_id', 'Order_address', 'Order_Type','Quentity','Order_Product_Amount','Order_Gst_Amount','order_amount','Use_coupon','Cupon_Code','Cupon_Discount','Amount','Payment_Status','Order_Status_Set','Payment_Method','shipping_charge','shipping_Payment_Status','shipping_Payment_Method','Order_Date','delivery_Date','Payment_Date')
    list_filter = ('User','Order_Type','Order_Type')
admin.site.register(AwOrders,AwOrdersAdmin)

class AwAddToCardAdmin(ImportExportModelAdmin):
    list_display = ('User','Cookies_id','Order_Type','Product_Cellar','Product_Delivered','Event_Ticket','Case_Formate','Quentity','Old_Cost','Date')
    # list_filter = ('User','Event_Ticket','Product_Cellar','Product_Delivered','Date','Year',)
admin.site.register(AwAddToCard,AwAddToCardAdmin)


class AwOrederItemAdmin(ImportExportModelAdmin):
    list_display = ('User','Order_id', 'Product_Cellar','Product_Delivered','Event_Ticket','Year','Case_Formate_text','Case_Formate','Cost_of_product','Gst','Duty','Quentity','Total_cost')
    list_filter = ('User','Order_id','Product_Cellar','Quentity','Year',)
admin.site.register(AwOrederItem,AwOrederItemAdmin)

class AwOrderNoteAdmin(ImportExportModelAdmin):
    list_display = ('User','Order_id', 'Display_Status','Note','Attachment', 'Date')
admin.site.register(AwOrderNote,AwOrderNoteAdmin)