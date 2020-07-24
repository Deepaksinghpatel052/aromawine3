from django.contrib import admin
from .models import User_Service_Interests
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class User_Service_InterestsAdmin(ImportExportModelAdmin):
    list_display = ('Service_interests_by_user', 'Interested_User','Service_interest','Date')
    list_filter = ('Date','Service_interests_by_user','Interested_User',)
admin.site.register(User_Service_Interests,User_Service_InterestsAdmin)

