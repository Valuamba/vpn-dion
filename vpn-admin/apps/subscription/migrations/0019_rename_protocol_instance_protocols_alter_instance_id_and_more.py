# Generated by Django 4.0.5 on 2022-07-27 17:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0018_alter_instance_id_remove_instance_protocol_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instance',
            old_name='protocol',
            new_name='protocols',
        ),
        migrations.AlterField(
            model_name='instance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6f77faf8-6f38-423b-b79c-e3909182c04e'), editable=False),
        ),
        migrations.AlterField(
            model_name='vpnitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6f77faf8-6f38-423b-b79c-e3909182c04e'), editable=False),
        ),
        migrations.AlterField(
            model_name='vpnsubscription',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6f77faf8-6f38-423b-b79c-e3909182c04e'), editable=False),
        ),
    ]
