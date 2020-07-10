from django.contrib import admin
from .models import AwVarietals
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwVarietalsAdmin(ImportExportModelAdmin):
    list_display = ('Varietals_Name','Slug','Status', 'Created_by','Created_date','Updated_by','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwVarietals,AwVarietalsAdmin)