from django.contrib import admin
from .models import User
from server.models import ServerReservation


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('User_name', 'display_occupied_server')

    def display_occupied_server(self, obj):
        pass



admin.site.register(User, UserAdmin)
