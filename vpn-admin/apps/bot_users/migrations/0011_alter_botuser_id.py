# Generated by Django 3.2.7 on 2022-09-01 06:17

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
            field=models.UUIDField(default=uuid.UUID('46ca2cf1-a706-49a0-958f-2149f3bd62dc'), editable=False),
        ),
    ]