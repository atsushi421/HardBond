# Generated by Django 3.2.6 on 2021-08-14 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20210815_0438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='user_name',
            new_name='obon_name',
        ),
    ]
