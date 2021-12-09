from django.contrib import admin
from .models import *
from django.utils.html import format_html


class ServerAdmin(admin.ModelAdmin):
    # actions = ['online_Server', 'offline_Server']
    list_display = ('server_name', "server_status", 'enable')
    list_editable = ['enable']

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
    list_display = ('server_id', 'user_id', 'reservation_time', 'end_time')


# Register your models here.
admin.site.register(ServerManagement, ServerAdmin)
admin.site.register(ServerReservation, ReservationAdmin)
