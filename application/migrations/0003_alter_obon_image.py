# Generated by Django 3.2.6 on 2021-08-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_obon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obon',
            name='image',
            field=models.ImageField(default='bonta.png', upload_to=''),
        ),
    ]