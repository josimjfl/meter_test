# Generated by Django 5.0.6 on 2024-09-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_data', '0008_remove_results_test_to_results_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_data',
            name='install_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
