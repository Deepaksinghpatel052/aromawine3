from django.contrib import admin
from .models import AwRegion
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwRegionAdmin(ImportExportModelAdmin):
    list_display = ('Region_Name', 'Country','Status', 'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwRegion,AwRegionAdmin)