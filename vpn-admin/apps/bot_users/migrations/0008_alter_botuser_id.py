# Generated by Django 4.0.5 on 2022-08-11 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0007_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('970853a1-21b3-4f49-9be2-3cff7cfce6e1'), editable=False),
        ),
    ]