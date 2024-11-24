# Generated by Django 5.0.6 on 2024-11-23 03:01

import accounts.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('balance_reg', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(blank=True, max_length=20, null=True)),
                ('cmo', models.CharField(blank=True, max_length=20, null=True)),
                ('received_by', models.CharField(blank=True, max_length=100, null=True)),
                ('meter_no', models.CharField(blank=True, max_length=100, null=True)),
                ('reading', models.CharField(blank=True, max_length=50, null=True)),
                ('main_seal', models.CharField(blank=True, max_length=50, null=True)),
                ('body_seal1', models.CharField(blank=True, max_length=50, null=True)),
                ('body_seal2', models.CharField(blank=True, max_length=50, null=True)),
                ('mfg', models.CharField(blank=True, max_length=50, null=True)),
                ('total_j31', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issue_created_by', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balance_reg.item')),
                ('office', models.ForeignKey(default=accounts.models.default_office, on_delete=django.db.models.deletion.CASCADE, to='accounts.office')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issue_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SealIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, default='J-31', max_length=20, null=True)),
                ('cmo', models.CharField(blank=True, max_length=20, null=True)),
                ('book', models.CharField(blank=True, max_length=10, null=True)),
                ('account', models.CharField(blank=True, max_length=10, null=True)),
                ('received_by', models.CharField(blank=True, max_length=100, null=True)),
                ('main_seal', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seal_issue_created_by', to=settings.AUTH_USER_MODEL)),
                ('office', models.ForeignKey(default=accounts.models.default_office, on_delete=django.db.models.deletion.CASCADE, to='accounts.office')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seal_issue_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
