from django.contrib import admin
from .models import AwWineRecipes
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwWineRecipesAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Slug','Created_by','Created_date','Updated_by','Updated_date')
    list_filter = ('Created_date',)
admin.site.register(AwWineRecipes,AwWineRecipesAdmin)
