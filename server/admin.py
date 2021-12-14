from django.contrib import admin
from .models import *
from django.utils.html import format_html


class ServerAdmin(admin.ModelAdmin):
    exclude = ['server_name']
    # actions = ['online_Server', 'offline_Server']
    list_display = ('server_name', "server_status", 'enable', 'user_occupied')
    list_editable = ['enable']

    def user_occupied(self, obj):
        result = ServerReservation.objects.filter(server_id=obj.id)
        for var in result:
            if var.reservation_time < timezone.now() < var.end_time:
                return var.user_id
        return None
    # def online_Server(self, request, queryset):
    #     queryset.update(enable=True)
    #
    # def offline_Server(self, request, queryset):
    #     queryset.update(enable=False)

    def server_status(self, obj):
        if obj.enable is True:
            return "Online"
        return "Offline"


class ReservationAdmin(admin.ModelAdmin):
    model = ServerReservation
    list_display = ('server_id', 'user_id', 'reservation_time', 'end_time', 'system_occupied')


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['server_id'].queryset = ServerManagement.objects.filter(enable__iexact=1)
        return form

    def system_occupied(self, obj):
        if obj.reservation_time < timezone.now() < obj.end_time:
            return "Occupied"
        elif timezone.now() > obj.end_time:
            return "Completed"
        return "On waiting"

# Register your models here.
admin.site.register(ServerManagement, ServerAdmin)
admin.site.register(ServerReservation, ReservationAdmin)

admin.site.register(CpuUsage)
