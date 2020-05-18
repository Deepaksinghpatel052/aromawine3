from django.contrib import admin
from .models import AwClassification
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwClassificationAdmin(ImportExportModelAdmin):
    list_display = ('Classification_Name', 'Status', 'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwClassification,AwClassificationAdmin)
