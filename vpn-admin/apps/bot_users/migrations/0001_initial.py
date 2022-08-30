# Generated by Django 3.2.7 on 2022-08-25 23:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='User ID')),
                ('user_name', models.CharField(blank=True, max_length=200, verbose_name='User Name')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Last Name')),
                ('is_bot_blocked', models.BooleanField(default=False, verbose_name='Is Bot Blocked by User')),
                ('referral_value', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Referral value')),
                ('id', models.UUIDField(default=uuid.UUID('72c0c8da-9471-4aeb-bf19-0bc1c246fedf'), editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bot_user',
            },
        ),
        migrations.CreateModel(
            name='ReferralItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_activated_reward', models.BooleanField(default=False, verbose_name='Is activated reward')),
                ('referral_owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='referrals', to='bot_users.botuser')),
                ('referred_user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='referral_item', to='bot_users.botuser')),
            ],
        ),
    ]
