# Generated by Django 4.0.5 on 2022-08-06 11:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_protocol', '0005_alter_vpnprotocol_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpnprotocol',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a3957fee-6a28-4286-95e2-59d5ebecdd2f'), editable=False),
        ),
    ]
