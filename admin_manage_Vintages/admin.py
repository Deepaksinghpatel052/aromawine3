from django.contrib import admin
from .models import AwVintages
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwVintagesAdmin(ImportExportModelAdmin):
    list_display = ('Vintages_Year','Status', 'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwVintages,AwVintagesAdmin)
