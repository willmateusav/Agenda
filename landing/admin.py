from django.contrib import admin
from .models import appointment, Visit
import csv
from django.http import HttpResponse

def download_csv(modeladmin, request, queryset):
    import csv
    f = open('agenda.csv', 'w', encoding='utf-8-sig')
    writer = csv.writer(f)
    writer.writerow(["first_name", "email", "date", "hour"])
    for s in queryset:
        writer.writerow([s.first_name, s.email, s.date, s.hour])
    
    f.close()

    f = open('agenda.csv', 'r')
    response = HttpResponse(f, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
    return response

class AppointmentFormAdmin(admin.ModelAdmin):
    model = appointment
    list_display = ('first_name', 'email', 'date', 'hour')
    actions = [download_csv]
    def download_csv(self, request, queryset):
        None
    download_csv.short_description = "Download CSV file for selected stats."

class VisitAdmin(admin.ModelAdmin):
    model = Visit
    list_display = ('ip_address_V', 'visit_day', 'location_country', 'location_city', 'device_type', 'browser_type', 'browser_version', 'os_type', 'os_version')


admin.site.register(appointment, AppointmentFormAdmin)
admin.site.register(Visit, VisitAdmin)