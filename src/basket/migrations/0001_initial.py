# Generated by Django 3.1.4 on 2021-01-02 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('phones', '0009_auto_20210101_2312'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(max_length=3, verbose_name='تعداد')),
                ('add_datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='زمان اضافه کردن')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.phone', verbose_name='تلفن همراه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]