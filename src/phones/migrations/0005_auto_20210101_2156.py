# Generated by Django 3.1.4 on 2021-01-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_phone_other_ui'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='back_camera_other',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='سایر'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='body_other',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='سایر'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='display_other',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='سایر'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='front_camera_other',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='سایر'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='hardware_other',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='سایر'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='storage_other',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='سایر'),
        ),
    ]
