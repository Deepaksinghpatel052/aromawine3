from django.contrib import admin
from .models import AwAddressBook
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwAddressBookAdmin(ImportExportModelAdmin):
    list_display = ('User', 'First_Name','Last_Name' ,'Email','Pnone_no','Conpany_Name','Country','Address','Address_2','City','Postcode','Landmark','Create_Date','Update_Date')
    list_filter = ('User','City',)
admin.site.register(AwAddressBook,AwAddressBookAdmin)
