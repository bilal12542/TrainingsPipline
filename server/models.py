from django.db import models
from django.db.models import Q
from django.utils import timezone
import user.models
import datetime
from django.core.exceptions import ValidationError


# Create your models here.

class ServerManagement(models.Model):
    server_name = models.CharField(max_length=255)
    ip_addr = models.CharField(default='0.0.0.0', max_length=255)
    ram = models.FloatField(max_length=3)
    processor = models.CharField(max_length=255)
    enable = models.BooleanField(default=False, null=False)

    # class Meta:
    #     constraints = [models.CheckConstraint(check=Q(server_name__gte='Server'), name="server name")]

    def __str__(self):
        return self.server_name


class ServerReservation(models.Model):
    server_id = models.ForeignKey(ServerManagement, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user.models.User, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now() + datetime.timedelta(hours=2))

    def clean(self):
        if self.reservation_time > self.end_time:
            raise ValidationError('Start date is after end date')
    # @property
    # def available(self):
    #     if self.end_time > timezone.now().strftime('%Y-%m-%d %H:%M:%S'):
    #         return False
    #     return True
