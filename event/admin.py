from django.contrib import admin
from manage_event.models import AwEvent,AwEventType
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwEventAdmin(ImportExportModelAdmin):
    list_display = ('Event_name','Slug','Start_Date', 'End_Date','ticket_pr_person','ticket_price','Status','Created_date','Updated_by','Updated_date')
    list_filter = ('Start_Date','End_Date','Created_date',)

admin.site.register(AwEvent,AwEventAdmin)



class AwEventTypeAdmin(ImportExportModelAdmin):
    list_display = ('Type','Slug','Created_date')


admin.site.register(AwEventType,AwEventTypeAdmin)
