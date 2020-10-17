from django.contrib import admin
from .models import AwWishList
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwWishListeAdmin(ImportExportModelAdmin):
    list_display = ('user_info', 'Product','Case_Formate','Created_date')
    list_filter = ('user_info', 'Case_Formate',)
admin.site.register(AwWishList,AwWishListeAdmin)
