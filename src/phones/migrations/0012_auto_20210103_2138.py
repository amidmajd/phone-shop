# Generated by Django 3.1.4 on 2021-01-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0011_auto_20210103_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='storage_type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='کارت حافظه'),
        ),
    ]