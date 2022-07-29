# Generated by Django 4.0.5 on 2022-07-24 13:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_alter_vpnsubscription_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpnsubscription',
            name='currency',
            field=models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD')], max_length=10, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='vpnsubscription',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d0bf1a0f-35e1-4580-8f4a-a351bdfc6197'), editable=False),
        ),
    ]
