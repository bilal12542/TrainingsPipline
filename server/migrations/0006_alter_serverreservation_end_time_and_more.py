# Generated by Django 4.0 on 2021-12-09 10:11

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_rename_server_serverreservation_server_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverreservation',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 9, 12, 11, 13, 407740, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='serverreservation',
            name='reservation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
