# Generated by Django 5.0.6 on 2024-08-13 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue_item', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issueitem',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='sealissue',
            options={'ordering': ['-id']},
        ),
    ]
