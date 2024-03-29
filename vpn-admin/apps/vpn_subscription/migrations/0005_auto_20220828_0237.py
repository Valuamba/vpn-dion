# Generated by Django 3.2.7 on 2022-08-27 23:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_subscription', '0004_alter_vpnpaymenttransaction_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpnsubscription',
            name='days_duration',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Days duration'),
        ),
        migrations.AlterField(
            model_name='vpnsubscription',
            name='month_duration',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Month duration'),
        ),
    ]
