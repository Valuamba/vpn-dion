# Generated by Django 4.0.5 on 2022-08-11 16:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0005_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('03d83d2a-00e7-4de0-9bc9-6919fcbf3699'), editable=False),
        ),
    ]