# Generated by Django 3.1.4 on 2021-01-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0009_auto_20210101_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='موجود'),
        ),
    ]
