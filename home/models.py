from django.db import models

# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="عنوان")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    location = models.CharField(max_length=255, verbose_name="موقعیت / آدرس")
    opening_hours = models.CharField(max_length=255, blank=True, null=True, verbose_name="ساعات کاری")

    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    phone_number_2 = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره تماس دوم")

    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")

    whatsapp = models.CharField(max_length=15, blank=True, null=True, verbose_name="واتساپ")
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name="تلگرام")

    map_link = models.CharField(blank=True, null=True, verbose_name="لینک گوگل مپ", max_length=100000)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else self.location