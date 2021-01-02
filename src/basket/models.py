from django.db import models
from django.contrib.auth.models import User
from phones.models import Phone
from django.utils import timezone

MAX_ORDER_COUNT = 100


class Basket(models.Model):
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, verbose_name='تلفن همراه', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(
        verbose_name='تعداد',
        default=1,
        choices=[(i, i) for i in range(1, MAX_ORDER_COUNT + 1)]
    )
    add_datetime = models.DateTimeField(verbose_name='زمان اضافه کردن', default=timezone.now, editable=False)

    def __str__(self):
        return f'user:{self.user}, phone:{self.phone}, count:{self.count}'
