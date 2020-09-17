from django.contrib import admin
from .models import AwNotification
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwNotificationAdmin(ImportExportModelAdmin):
    list_display = ('user','Send_Status', 'Created_by', 'Created_by','Created_date','Read_Status','Read_date')
admin.site.register(AwNotification,AwNotificationAdmin)