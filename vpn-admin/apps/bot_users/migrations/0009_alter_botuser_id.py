# Generated by Django 3.2.7 on 2022-08-28 00:05

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
            field=models.UUIDField(default=uuid.UUID('ccdee7b0-ad52-4ab8-ad16-f7656ed8ab87'), editable=False),
        ),
    ]
