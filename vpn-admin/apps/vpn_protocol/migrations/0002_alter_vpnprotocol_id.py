# Generated by Django 4.0.5 on 2022-07-30 10:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_protocol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpnprotocol',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e6a5c434-c2b8-4189-93b7-d915794ffdc5'), editable=False),
        ),
    ]
