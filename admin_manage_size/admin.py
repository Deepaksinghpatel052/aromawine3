from django.contrib import admin
from .models import AwSize
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwSizeAdmin(ImportExportModelAdmin):
    list_display = ('Bottle_Size', 'Status', 'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwSize,AwSizeAdmin)
