# Generated by Django 3.2.6 on 2021-08-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Bonta', max_length=255)),
                ('money', models.IntegerField(default=1000)),
                ('image', models.ImageField(upload_to='')),
                ('material', models.CharField(default='wood', max_length=255)),
                ('size', models.IntegerField(default=5)),
                ('wise', models.IntegerField(default=5)),
                ('weight', models.IntegerField(default=5)),
                ('motivation', models.IntegerField(default=5)),
            ],
        ),
    ]
