# Generated by Django 4.0.5 on 2022-07-27 06:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0014_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3a5bedf5-6ed1-4f27-8125-a2761987f888'), editable=False),
        ),
    ]
