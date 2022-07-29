# Generated by Django 4.0.5 on 2022-07-27 17:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0016_instance_labels_alter_instance_id_alter_vpnitem_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instance',
            old_name='labels',
            new_name='protocol',
        ),
        migrations.AlterField(
            model_name='instance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1d9411b5-ba70-41f7-8739-340eefc3007a'), editable=False),
        ),
        migrations.AlterField(
            model_name='vpnitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1d9411b5-ba70-41f7-8739-340eefc3007a'), editable=False),
        ),
        migrations.AlterField(
            model_name='vpnsubscription',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1d9411b5-ba70-41f7-8739-340eefc3007a'), editable=False),
        ),
    ]
