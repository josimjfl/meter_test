# Generated by Django 5.0.6 on 2024-07-30 10:58

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
            name='uploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('url', models.TextField(default=' ', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('kh', models.CharField(blank=True, max_length=5, null=True)),
                ('meter_class', models.CharField(blank=True, max_length=5, null=True)),
                ('meter_type', models.CharField(blank=True, max_length=20, null=True)),
                ('LL_TA', models.CharField(default=1, max_length=5)),
                ('FL_TA', models.CharField(default=10, max_length=5)),
                ('LL_rev', models.CharField(default=2, max_length=5)),
                ('FL_rev', models.CharField(default=10, max_length=5)),
                ('standerd_rev_req_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('standerd_rev_req_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('item_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balance_reg.item')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(blank=True, max_length=1000, null=True)),
                ('remark', models.TextField(blank=True, choices=[('ব্যবহার উপযোগী।', 'ব্যবহার উপযোগী।'), ('ব্যবহার অনুপযোগী।', 'ব্যবহার অনুপযোগী।'), ('পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।', 'পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।')], null=True)),
                ('office', models.ForeignKey(default=accounts.models.get_office, on_delete=django.db.models.deletion.CASCADE, to='accounts.office')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tested_meter_no', models.CharField(blank=True, max_length=20, null=True)),
                ('reading_as_found', models.CharField(default='x', max_length=20)),
                ('reading_as_left', models.CharField(default='x', max_length=20)),
                ('multiplier', models.CharField(default=1, max_length=20)),
                ('cmo', models.CharField(blank=True, max_length=20, null=True)),
                ('book', models.CharField(blank=True, max_length=3, null=True)),
                ('account', models.CharField(blank=True, max_length=4, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=30, null=True)),
                ('meter_class', models.CharField(blank=True, max_length=5, null=True)),
                ('meter_item', models.CharField(blank=True, max_length=100, null=True)),
                ('kh', models.CharField(blank=True, max_length=5, null=True)),
                ('LL_TA', models.CharField(default=1, max_length=5)),
                ('FL_TA', models.CharField(default=10, max_length=5)),
                ('LL_rev', models.CharField(default=2, max_length=5)),
                ('FL_rev', models.CharField(default=10, max_length=5)),
                ('as_found_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('as_found_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('percent_found_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('percent_found_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('error_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('error_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('as_left_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('as_left_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('percent_left_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('percent_left_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('error_left_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('error_left_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('standerd_rev_req_ll', models.CharField(blank=True, max_length=10, null=True)),
                ('standerd_rev_req_fl', models.CharField(blank=True, max_length=10, null=True)),
                ('terminal_seal', models.CharField(blank=True, max_length=50, null=True)),
                ('terminal_seal_no', models.CharField(blank=True, max_length=20, null=True)),
                ('terminal_seal_missing', models.CharField(blank=True, max_length=100, null=True)),
                ('body_seal', models.CharField(blank=True, max_length=50, null=True)),
                ('glass_cover', models.CharField(blank=True, max_length=100, null=True)),
                ('test_clip', models.CharField(blank=True, max_length=100, null=True)),
                ('remove_cause', models.CharField(blank=True, max_length=255, null=True)),
                ('remove_date', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, default='মিটারটি ভালো আছে।', max_length=200, null=True)),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('cmo_type', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_order', models.CharField(default='-', max_length=100)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('checked_date', models.DateTimeField(blank=True, null=True)),
                ('counter_sign_date', models.DateTimeField(blank=True, null=True)),
                ('received_date', models.DateTimeField(blank=True, null=True)),
                ('checked_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_by', to=settings.AUTH_USER_MODEL)),
                ('counter_sign_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counter_sign_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='td_created_by', to=settings.AUTH_USER_MODEL)),
                ('office', models.ForeignKey(default=accounts.models.get_office, on_delete=django.db.models.deletion.CASCADE, to='accounts.office')),
                ('received_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='td_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
