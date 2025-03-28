# Generated by Django 5.1.6 on 2025-03-04 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('new', 'New'), ('call_attempt', 'Call Attempt'), ('sale', 'Sale'), ('no_sale', 'No Sale')], default='new', max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission_status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lead', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.lead')),
            ],
        ),
    ]
