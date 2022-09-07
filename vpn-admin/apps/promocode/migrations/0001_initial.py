# Generated by Django 3.2.7 on 2022-09-07 15:41

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot_users', '0016_alter_botuser_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('promocode', models.CharField(max_length=100, unique=True, verbose_name='Promocode')),
                ('expires', models.DateTimeField(verbose_name='Expires')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Discount')),
                ('applied_by_users', models.ManyToManyField(related_name='promocodes', to='bot_users.BotUser')),
            ],
            options={
                'db_table': 'promocode',
            },
        ),
    ]
