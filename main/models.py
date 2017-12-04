# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class MainSlider(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки для слайдера'
        verbose_name = 'Картинка для слайдера'

    image = models.ImageField(upload_to='slider_images', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Краткое описание')

    def __unicode__(self):
        return self.title


class Banners(models.Model):
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    image = models.ImageField(upload_to='banners', verbose_name='Баннер')

    def __unicode__(self):
        return 'banner obj'
        # return str(self.image)
