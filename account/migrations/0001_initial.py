# Generated by Django 2.2.16 on 2020-09-21 15:30

import account.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.TextField(unique=True)),
                ('realname', models.TextField(null=True)),
                ('email', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('schoolssn', models.IntegerField(default=0)),
                ('admin_type', models.TextField(default='Regular User')),
                ('problem_permission', models.TextField(default='None')),
                ('reset_password_token', models.TextField(null=True)),
                ('reset_password_token_expire_time', models.DateTimeField(null=True)),
                ('auth_token', models.TextField(null=True)),
                ('two_factor_auth', models.BooleanField(default=False)),
                ('tfa_token', models.TextField(null=True)),
                ('session_keys', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('open_api', models.BooleanField(default=False)),
                ('open_api_appkey', models.TextField(null=True)),
                ('is_disabled', models.BooleanField(default=False)),
                ('is_allowed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acm_problems_status', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('oi_problems_status', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('real_name', models.TextField(null=True)),
                ('avatar', models.TextField(default='/public/avatar/default.png')),
                ('blog', models.URLField(null=True)),
                ('mood', models.TextField(null=True)),
                ('github', models.TextField(null=True)),
                ('school', models.TextField(null=True)),
                ('major', models.TextField(null=True)),
                ('language', models.TextField(null=True)),
                ('accepted_number', models.IntegerField(default=0)),
                ('total_score', models.BigIntegerField(default=0)),
                ('submission_number', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
