# Generated by Django 5.0.6 on 2024-09-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customuser_date_alter_standard_meter_from_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date',
            field=models.DateField(default='2024-09-29'),
        ),
        migrations.AlterField(
            model_name='standard_meter',
            name='from_date',
            field=models.DateField(default='2024-09-29'),
        ),
    ]
