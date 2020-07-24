from django.contrib import admin
from .models import AwInterestType,Service_Interests
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwInterestTypeAdmin(ImportExportModelAdmin):
    list_display = ('Type', 'Status','Created_by','Created_date','Updated_by','Updated_date')
    list_filter = ('Created_date','Type','Updated_date',)
admin.site.register(AwInterestType,AwInterestTypeAdmin)



class Service_InterestsAdmin(ImportExportModelAdmin):
    list_display = ('Service_interests_name', 'Select_Type','Date')
    list_filter = ('Service_interests_name','Select_Type')
admin.site.register(Service_Interests,Service_InterestsAdmin)

