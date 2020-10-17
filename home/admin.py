from django.contrib import admin
from .models import AwAboutAromaWines,AwCmsPaage
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwAboutAromaWinesAdmin(ImportExportModelAdmin):
    list_display = ('Title','Create_date')
admin.site.register(AwAboutAromaWines,AwAboutAromaWinesAdmin)

class AwCmsPaageAdmin(ImportExportModelAdmin):
    list_display = ('Title','Slug','Background_Image','Short_description_Show_in_Footer','Publish','Create_date')
admin.site.register(AwCmsPaage,AwCmsPaageAdmin)

