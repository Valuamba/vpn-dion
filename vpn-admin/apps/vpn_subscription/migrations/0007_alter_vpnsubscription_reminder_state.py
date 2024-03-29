# Generated by Django 3.2.7 on 2022-09-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_subscription', '0006_auto_20220901_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpnsubscription',
            name='reminder_state',
            field=models.IntegerField(choices=[(3, 'Reminded for three days'), (7, 'Reminded for seven days'), (1, 'Reminded for one day'), (0, 'Ended')], verbose_name='Reminder status'),
        ),
    ]
