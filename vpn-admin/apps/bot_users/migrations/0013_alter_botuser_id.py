# Generated by Django 4.0.5 on 2022-07-27 06:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0012_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e1e0148-9481-46f4-a519-be3e9c2182bd'), editable=False),
        ),
    ]
