from django.contrib import admin
from .models import ServerManagement
from django.utils.html import format_html


class ServerAdmin(admin.ModelAdmin):
    model = ServerManagement
    actions = ['available_Server', 'disable_Server']
    list_display = ('server_name', 'available')

    def available_Server(self, request, queryset):
        queryset.update(available=True)

    def disable_Server(self, request, queryset):
        queryset.update(available=False)

    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Deposit</a>&nbsp;'
            '<a class="button" href="{}">Withdraw</a>',
        )


# Register your models here.
admin.site.register(ServerManagement, ServerAdmin)
