# Generated by Django 5.1.4 on 2024-12-17 14:23

import django.db.models.deletion
import secrets
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('account_id', models.UUIDField(unique=True)),
                ('account_name', models.CharField(max_length=50)),
                ('app_secret_token', models.CharField(default=secrets.token_urlsafe, editable=False, max_length=50)),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('http_method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT')], max_length=10)),
                ('headers', models.JSONField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='webhook_app.accounts')),
            ],
            options={
                'db_table': 'destinations',
            },
        ),
    ]