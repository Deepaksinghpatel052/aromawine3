from django.contrib import admin
from .models import AwBanners
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwBannersAdmin(ImportExportModelAdmin):
    list_display = ('Title', 'Type','Status' ,'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwBanners,AwBannersAdmin)