# Generated by Django 3.2.7 on 2022-09-07 15:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0015_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a7d0f7df-084a-4935-9ea9-05a2639a3b8a'), editable=False),
        ),
    ]