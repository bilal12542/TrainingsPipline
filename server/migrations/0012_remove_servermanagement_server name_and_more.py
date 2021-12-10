# Generated by Django 4.0 on 2021-12-10 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_alter_servermanagement_id_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='servermanagement',
            name='server name',
        ),
        migrations.AlterField(
            model_name='servermanagement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='servermanagement',
            name='server_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='serverreservation',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 10, 4, 21, 569487, tzinfo=utc)),
        ),
    ]
