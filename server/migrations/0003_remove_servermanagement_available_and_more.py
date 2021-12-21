# Generated by Django 4.0 on 2021-12-09 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('server', '0002_servermanagement_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servermanagement',
            name='available',
        ),
        migrations.AlterField(
            model_name='servermanagement',
            name='ram',
            field=models.FloatField(max_length=3),
        ),
        migrations.CreateModel(
            name='ServerReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.servermanagement')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
