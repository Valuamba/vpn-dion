# Generated by Django 4.0.5 on 2022-08-11 16:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot_users', '0006_alter_botuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ea1f7e08-245e-459f-ae34-7010cc63d785'), editable=False),
        ),
    ]
