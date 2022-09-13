# Generated by Django 3.2.7 on 2022-09-12 16:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotMessageLocale',
            fields=[
                ('alias', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=2000)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'message_locale',
            },
        ),
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='User ID')),
                ('user_name', models.CharField(blank=True, max_length=200, verbose_name='User Name')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Last Name')),
                ('is_bot_blocked', models.BooleanField(default=False, verbose_name='Is Bot Blocked by User')),
                ('referral_value', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Referral value')),
                ('id', models.UUIDField(default=uuid.UUID('3824bf96-3193-497b-88d4-6a6504c10387'), editable=False)),
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('referral_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='bot.botuser')),
                ('referred_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='referral_item', to='bot.botuser')),
            ],
            options={
                'db_table': 'referral_items',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField()),
                ('text', models.TextField()),
                ('status', models.BooleanField(blank=True, null=True)),
                ('receive_date', models.DateTimeField(auto_now_add=True)),
                ('answer_date', models.DateTimeField(blank=True, null=True)),
                ('admin_message', models.TextField(blank=True, null=True)),
                ('admin_message_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='feedback_messages', to='bot.botuser')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'db_table': 'feedback_messages',
                'ordering': ['status', '-receive_date'],
            },
        ),
    ]
