# Generated by Django 3.2.6 on 2021-08-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]
