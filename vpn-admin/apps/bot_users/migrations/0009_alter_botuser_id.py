# Generated by Django 4.0.5 on 2022-08-12 20:32

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
            field=models.UUIDField(default=uuid.UUID('5d39c71b-88da-48ce-a3b1-5d84786f3452'), editable=False),
        ),
    ]
