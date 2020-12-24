from django.contrib import admin
from .models import AwWinePalateCategories, AwWinePalateFlavors, AwUserPalateWine
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwWinePalateCategoriesAdmin(ImportExportModelAdmin):
    list_display = ('Category_name','Category_Id','Category_Color','Category_Type', 'Created_date')
admin.site.register(AwWinePalateCategories,AwWinePalateCategoriesAdmin)



class AwUserPalateWineAdmin(ImportExportModelAdmin):
    list_display = ('User','Category_name','Type', 'CategoryNameAndType','Created_date')
admin.site.register(AwUserPalateWine,AwUserPalateWineAdmin)


class AwWinePalateFlavorsAdmin(ImportExportModelAdmin):
    list_display = ('Category', 'Type')
admin.site.register(AwWinePalateFlavors,AwWinePalateFlavorsAdmin)

