# Generated by Django 3.2.10 on 2021-12-19 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0017_alter_serverreservation_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverreservation',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
