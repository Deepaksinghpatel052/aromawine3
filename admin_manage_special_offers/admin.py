from django.contrib import admin
from .models import AwSpecialOffers
from import_export.admin import ImportExportModelAdmin


# Register your models here.


class AwSpecialOffersAdmin(ImportExportModelAdmin):
    list_display = ('Title', 'Priority_set', 'Banner_Image', 'Link', 'Created_by', 'Created_date')

admin.site.register(AwSpecialOffers, AwSpecialOffersAdmin)