from django.contrib import admin
from .models import AwSetTo,AwProducers
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AwSetToAdmin(ImportExportModelAdmin):
    list_display = ('Title', 'Status', 'Created_date')

class AwProducersAdmin(ImportExportModelAdmin):
    list_display = ('Winnery_Name', 'Status', 'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwSetTo,AwSetToAdmin)
admin.site.register(AwProducers,AwProducersAdmin)