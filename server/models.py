from django.db import models

# Create your models here.

class ServerManagement(models.Model):
    server_name = models.CharField(max_length=255)
    ram = models.FloatField(max_length=2)
    processor = models.FloatField(max_length=5)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.server_name

