# Generated by Django 4.0.5 on 2022-07-30 10:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_duration_tariff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpndurationprice',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2889e949-04d0-4adf-85e8-aff4dfac3ab3'), editable=False),
        ),
    ]
