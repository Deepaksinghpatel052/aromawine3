from django.contrib import admin
from .models import AwAboutAromaWines
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwAboutAromaWinesAdmin(ImportExportModelAdmin):
    list_display = ('Title','Create_date')

admin.site.register(AwAboutAromaWines,AwAboutAromaWinesAdmin)