# Generated by Django 4.0.5 on 2022-07-26 20:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0008_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ec03e4c7-82e4-4b68-a43a-49de857232ad'), editable=False),
        ),
    ]
