# Generated by Django 3.2.7 on 2022-09-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='expires',
            field=models.DateField(verbose_name='Expires'),
        ),
    ]
