from django.contrib import admin
from .models import AwAdminSetting, AwManageShipping,AwAllCountry
from import_export.admin import ImportExportModelAdmin
# Register your models here.


admin.site.register(AwAllCountry)


class AwAdminSettingAdmin(ImportExportModelAdmin):
    list_display = ('Project_Name','Project_Tag_Line', 'Duty', 'GST','Analytics','Facebook','Twitter','Linkedin','Instgram','Google','Yelp','EMAIL_HOST','EMAIL_USE_TLS','EMAIL_PORT','EMAIL_HOST_USER','EMAIL_HOST_PASSWORD')
admin.site.register(AwAdminSetting,AwAdminSettingAdmin)


class AwManageShippingAdmin(ImportExportModelAdmin):
    list_display = ('Country','min_ordr_amount', 'Shiping_Fees_min_order_amount', 'Create_date','Created_by')
admin.site.register(AwManageShipping,AwManageShippingAdmin)