# Generated by Django 4.0.5 on 2022-08-11 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageLocale',
            fields=[
                ('alias', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=1000)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'MessageLocale',
            },
        ),
    ]
