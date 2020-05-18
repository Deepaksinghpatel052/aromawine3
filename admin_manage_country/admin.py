from django.contrib import admin
from .models import AwCountry
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwCountryAdmin(ImportExportModelAdmin):
    list_display = ('Country_Name', 'Status', 'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwCountry,AwCountryAdmin)
