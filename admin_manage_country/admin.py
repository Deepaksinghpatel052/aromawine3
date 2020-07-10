from django.contrib import admin
from .models import AwCountry,AwCountryUser
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwCountryAdmin(ImportExportModelAdmin):
    list_display = ('Country_Name','Slug', 'Status', 'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)
admin.site.register(AwCountry,AwCountryAdmin)

class AwCountryUserAdmin(ImportExportModelAdmin):
    list_display = ('Country_Name', 'Code')
admin.site.register(AwCountryUser,AwCountryUserAdmin)

