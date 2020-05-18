from django.contrib import admin
from .models import AwCategory
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwCategoryesAdmin(ImportExportModelAdmin):
    list_display = ('Category_name', 'Title','Status' ,'Created_by','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)

admin.site.register(AwCategory,AwCategoryesAdmin)
