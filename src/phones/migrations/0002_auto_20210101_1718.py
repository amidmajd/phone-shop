# Generated by Django 3.1.4 on 2021-01-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.BigIntegerField(verbose_name='قیمت (تومان)'),
        ),
    ]
