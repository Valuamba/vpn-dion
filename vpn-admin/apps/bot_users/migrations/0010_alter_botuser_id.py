# Generated by Django 3.2.7 on 2022-08-28 01:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0009_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ecf55d9b-4890-4cec-bb9a-28a981c3aee6'), editable=False),
        ),
    ]
