# Generated by Django 5.0.6 on 2024-08-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='remark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
