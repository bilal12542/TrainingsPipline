from django.db import models
from django.utils import timezone
import user.models
import datetime


# Create your models here.

class ServerManagement(models.Model):
    server_name = models.CharField(max_length=255)
    ram = models.FloatField(max_length=3)
    processor = models.FloatField(max_length=5)
    enable = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.server_name


class ServerReservation(models.Model):
    server_id = models.ForeignKey(ServerManagement, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user.models.User, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now() + datetime.timedelta(hours=2))

    # @property
    # def available(self):
    #     if self.end_time > timezone.now().strftime('%Y-%m-%d %H:%M:%S'):
    #         return False
    #     return True
