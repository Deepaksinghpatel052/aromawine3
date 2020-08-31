from django.contrib import admin
from .models import AwPaymentMethod
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AwPaymentMethodAdmin(ImportExportModelAdmin):
    list_display = ('Name_on_Card','Card_Number','Expiry_Date','CVC_CVV','ZIP','Created_by','Created_date')
    list_filter = ('Created_by',)
admin.site.register(AwPaymentMethod,AwPaymentMethodAdmin)