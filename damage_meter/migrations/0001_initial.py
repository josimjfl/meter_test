# Generated by Django 5.0.6 on 2024-07-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order', models.CharField(max_length=100)),
                ('remark', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]