# Generated by Django 5.0.6 on 2024-09-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_data', '0003_alter_manufacturer_options_alter_results_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_data',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
