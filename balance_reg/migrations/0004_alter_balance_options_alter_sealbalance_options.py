# Generated by Django 5.0.6 on 2024-08-13 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balance_reg', '0003_sealbalance_remark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='balance',
            options={'ordering': ['date_start']},
        ),
        migrations.AlterModelOptions(
            name='sealbalance',
            options={'ordering': ['date_start']},
        ),
    ]
