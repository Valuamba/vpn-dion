# Generated by Django 4.0.5 on 2022-07-26 21:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0010_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b4e9fba5-43bc-472b-8289-44a3de01c39e'), editable=False),
        ),
    ]
