# Generated by Django 3.2.7 on 2022-09-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_country', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpncountry',
            name='locale_ru',
            field=models.CharField(default='Norway', max_length=200, verbose_name='Locale RU'),
            preserve_default=False,
        ),
    ]
