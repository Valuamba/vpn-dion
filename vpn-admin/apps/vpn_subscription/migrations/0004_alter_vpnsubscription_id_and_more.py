# Generated by Django 4.0.5 on 2022-08-01 07:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_subscription', '0003_alter_vpnsubscription_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpnsubscription',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6ae3a6b4-ad23-4372-ba98-25a65d5251c7'), editable=False),
        ),
        migrations.AlterField(
            model_name='vpnsubscription',
            name='status',
            field=models.CharField(choices=[('paid', 'On Payment'), ('waiting for payment', 'Waiting for payment'), ('payment_was_failed', 'Payment was failed')], max_length=100, verbose_name='Subscription status'),
        ),
    ]
