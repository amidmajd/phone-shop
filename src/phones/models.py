from django.db import models
from django.urls import reverse
from PIL import Image
import uuid
import os

base_image_dir = 'phones'

brand_choices = (
    ("Samsung", "Samsung"),
    ("Apple", "Apple"),
    ("Xiaomi", "Xiaomi"),
    ("Nokia", "Nokia"),
    ("Huawei", "Huawei"),
)


def max_of_brand_choices(iterable):
    return max([len(item[0]) for item in iterable])


class Phone(models.Model):
    id = models.CharField(
        verbose_name='شماره شناسایی',
        max_length=36,
        primary_key=True,
        default=uuid.uuid4,
        editable=True)
    brand = models.CharField(
        verbose_name='برند',
        max_length=max_of_brand_choices(brand_choices),
        choices=brand_choices)
    name = models.CharField(verbose_name='نام', max_length=64, unique=True)

    date = models.DateField(verbose_name='تاریخ تولید', blank=True, null=True)
    price = models.BigIntegerField(verbose_name='قیمت (تومان)')
    about = models.TextField(verbose_name='درباره', max_length=500, blank=True, null=True)
    image = models.ImageField(verbose_name='تصویر', default=os.path.join(base_image_dir, 'default.png'),
                              upload_to=base_image_dir,
                              )

    body_size = models.CharField(verbose_name='ابعاد', max_length=200, blank=True, null=True)
    body_weight = models.CharField(verbose_name='وزن', max_length=200, blank=True, null=True)
    body_structure = models.CharField(verbose_name='ساختار', max_length=200, blank=True, null=True)
    body_colors = models.CharField(verbose_name='رنگ‌بندی', max_length=200, blank=True, null=True)
    body_other = models.TextField(verbose_name='سایر', max_length=500, blank=True, null=True)

    display_type = models.CharField(verbose_name='نوع', max_length=200, blank=True, null=True)
    display_quality = models.CharField(verbose_name='وضوح', max_length=200, blank=True, null=True)
    display_colors = models.CharField(verbose_name='رنگ', max_length=200, blank=True, null=True)
    display_size = models.CharField(verbose_name='ابعاد', max_length=200, blank=True, null=True)
    display_other = models.TextField(verbose_name='سایر', max_length=500, blank=True, null=True)

    hardware_cpu = models.CharField(verbose_name='پردازنده اصلی', max_length=200, blank=True, null=True)
    hardware_gpu = models.CharField(verbose_name='پردازنده گرافیکی', max_length=200, blank=True, null=True)
    hardware_ram = models.CharField(verbose_name='حافظه رم', max_length=200, blank=True, null=True)
    hardware_battery = models.CharField(verbose_name='باتری', max_length=200, blank=True, null=True)
    hardware_other = models.TextField(verbose_name='سایر', max_length=500, blank=True, null=True)

    back_cam_pic_quality = models.CharField(verbose_name='وضوح تصویر', max_length=200, blank=True, null=True)
    back_cam_lens = models.TextField(verbose_name='لنز', max_length=500, blank=True, null=True)
    back_cam_vid_quality = models.CharField(verbose_name='وضوح فیلم', max_length=200, blank=True, null=True)
    back_cam_fps = models.CharField(verbose_name='نرخ فیلم برداری', max_length=200, blank=True, null=True)
    back_camera_other = models.TextField(verbose_name='سایر', max_length=500, blank=True, null=True)

    front_cam_pic_quality = models.CharField(verbose_name='وضوح تصویر', max_length=200, blank=True, null=True)
    front_cam_lens = models.TextField(verbose_name='لنز', max_length=500, blank=True, null=True)
    front_cam_vid_quality = models.CharField(verbose_name='وضوح فیلم', max_length=200, blank=True, null=True)
    front_cam_fps = models.CharField(verbose_name='نرخ فیلم برداری', max_length=200, blank=True, null=True)
    front_camera_other = models.TextField(verbose_name='سایر', max_length=500, blank=True, null=True)

    storage_type = models.CharField(verbose_name='نوع', max_length=200, blank=True, null=True)
    storage_size = models.CharField(verbose_name='حجم', max_length=200, blank=True, null=True)
    storage_other = models.TextField(verbose_name='سایر', max_length=500, blank=True, null=True)

    other_sim = models.CharField(verbose_name='نوع سیم کارت', max_length=200, blank=True, null=True)
    other_sim_count = models.CharField(verbose_name='تعداد سیم کارت', max_length=200, blank=True, null=True)
    other_os = models.CharField(verbose_name='سیستم عامل', max_length=200, blank=True, null=True)
    other_ui = models.CharField(verbose_name='رابط کاربری', max_length=200, blank=True, null=True)
    other_sensors = models.CharField(verbose_name='سنسور‌ها', max_length=200, blank=True, null=True)
    other_specials = models.TextField(verbose_name='خصوصیات ویژه', max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.brand}, {self.name}, {self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 512 or img.width > 512:
            img.thumbnail((512, 512))
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("phones:detail", kwargs={"id": self.id})
