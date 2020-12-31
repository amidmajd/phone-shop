# Generated by Django 3.1.4 on 2020-12-31 22:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False, verbose_name='شماره شناسایی')),
                ('brand', models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Xiaomi', 'Xiaomi'), ('Nokia', 'Nokia'), ('Huawei', 'Huawei')], max_length=7, verbose_name='برند')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='نام')),
                ('date', models.DateField(blank=True, null=True, verbose_name='تاریخ تولید')),
                ('price', models.BigIntegerField(verbose_name='قیمت')),
                ('about', models.TextField(blank=True, max_length=500, null=True, verbose_name='درباره')),
                ('image', models.ImageField(default='phones/default.png', upload_to='phones', verbose_name='تصویر')),
                ('body_size', models.CharField(blank=True, max_length=200, null=True, verbose_name='ابعاد')),
                ('body_weight', models.CharField(blank=True, max_length=200, null=True, verbose_name='وزن')),
                ('body_structure', models.CharField(blank=True, max_length=200, null=True, verbose_name='ساختار')),
                ('body_colors', models.CharField(blank=True, max_length=200, null=True, verbose_name='رنگ\u200cبندی')),
                ('body_other', models.TextField(blank=True, max_length=500, null=True, verbose_name='دیگر')),
                ('display_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='نوع')),
                ('display_colors', models.CharField(blank=True, max_length=200, null=True, verbose_name='رنگ')),
                ('display_size', models.CharField(blank=True, max_length=200, null=True, verbose_name='ابعاد')),
                ('display_quality', models.CharField(blank=True, max_length=200, null=True, verbose_name='وضوح')),
                ('display_other', models.TextField(blank=True, max_length=500, null=True, verbose_name='دیگر')),
                ('hardware_cpu', models.CharField(blank=True, max_length=200, null=True, verbose_name='پردازنده اصلی')),
                ('hardware_gpu', models.CharField(blank=True, max_length=200, null=True, verbose_name='پردازنده گرافیکی')),
                ('hardware_ram', models.CharField(blank=True, max_length=200, null=True, verbose_name='حافظه RAM')),
                ('hardware_battery', models.CharField(blank=True, max_length=200, null=True, verbose_name='باتری')),
                ('hardware_other', models.TextField(blank=True, max_length=500, null=True, verbose_name='دیگر')),
                ('back_cam_pic_quality', models.CharField(blank=True, max_length=200, null=True, verbose_name='وضوح تصویر')),
                ('back_cam_lens', models.CharField(blank=True, max_length=200, null=True, verbose_name='لنز')),
                ('back_cam_vid_quality', models.CharField(blank=True, max_length=200, null=True, verbose_name='وضوح فیلم')),
                ('back_cam_fps', models.CharField(blank=True, max_length=200, null=True, verbose_name='نرخ فیلم برداری')),
                ('back_camera_other', models.TextField(blank=True, max_length=500, null=True, verbose_name='دیگر')),
                ('front_cam_pic_quality', models.CharField(blank=True, max_length=200, null=True, verbose_name='وضوح تصویر')),
                ('front_cam_lens', models.CharField(blank=True, max_length=200, null=True, verbose_name='لنز')),
                ('front_cam_vid_quality', models.CharField(blank=True, max_length=200, null=True, verbose_name='وضوح فیلم')),
                ('front_cam_fps', models.CharField(blank=True, max_length=200, null=True, verbose_name='نرخ فیلم برداری')),
                ('front_camera_other', models.TextField(blank=True, max_length=500, null=True, verbose_name='دیگر')),
                ('storage_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='نوع')),
                ('storage_size', models.CharField(blank=True, max_length=200, null=True, verbose_name='حجم')),
                ('storage_other', models.TextField(blank=True, max_length=500, null=True, verbose_name='دیگر')),
                ('other_sim', models.CharField(blank=True, max_length=200, null=True, verbose_name='نوع سیم کارت')),
                ('other_sim_count', models.CharField(blank=True, max_length=200, null=True, verbose_name='تعداد سیم کارت')),
                ('other_os', models.CharField(blank=True, max_length=200, null=True, verbose_name='سیستم عامل')),
                ('other_sensors', models.CharField(blank=True, max_length=200, null=True, verbose_name='سنسور\u200cها')),
                ('other_specials', models.TextField(blank=True, max_length=500, null=True, verbose_name='خصوصیات ویژه')),
            ],
        ),
    ]