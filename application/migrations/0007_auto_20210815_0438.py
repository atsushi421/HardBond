# Generated by Django 3.2.6 on 2021-08-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_result_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='user',
        ),
        migrations.AddField(
            model_name='result',
            name='user_name',
            field=models.CharField(default='ๅ็กใ', max_length=255),
        ),
    ]
