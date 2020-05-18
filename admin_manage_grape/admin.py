from django.contrib import admin
from .models import AwGrape
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AwGrapeAdmin(ImportExportModelAdmin):
    list_display = ('Grape_Name', 'Status', 'Created_date')

admin.site.register(AwGrape,AwGrapeAdmin)
# Register your models here.
