# Generated by Django 5.0.6 on 2024-08-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_date_alter_standard_meter_from_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date',
            field=models.DateField(default='2024-08-02'),
        ),
        migrations.AlterField(
            model_name='standard_meter',
            name='from_date',
            field=models.DateField(default='2024-08-02'),
        ),
    ]
