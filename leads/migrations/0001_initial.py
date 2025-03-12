# Generated by Django 5.1.7 on 2025-03-12 06:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('billing_address', models.CharField(blank=True, max_length=255)),
                ('street_address', models.CharField(blank=True, max_length=255)),
                ('suburb', models.CharField(blank=True, max_length=100)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('electricity', models.BooleanField(default=False)),
                ('gas', models.BooleanField(default=False)),
                ('water', models.BooleanField(default=False)),
                ('broadband', models.BooleanField(default=False)),
                ('move_in_date', models.DateField(blank=True, null=True)),
                ('rea_office', models.CharField(blank=True, max_length=255)),
                ('referred_agent_name', models.CharField(blank=True, max_length=255)),
                ('rea_software_used', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('new', 'New'), ('call_attempt', 'Call Attempt'), ('sale', 'Sale'), ('no_sale', 'No Sale')], default='new', max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
