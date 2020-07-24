from django.contrib import admin
from .models import AwMembership
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AwMembershipAdmin(ImportExportModelAdmin):
    list_display = ('Membership_name','min_price', 'max_price', 'Created_by','Created_date')
admin.site.register(AwMembership,AwMembershipAdmin)