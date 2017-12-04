# coding=utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

ad_type = (('sell', 'Продаю'), ('buy', 'Куплю'), ('change', 'Меняю'), ('rent', 'Аренда'), ('offers', 'Услуги'))
Category_type = (
    ('stock_raising', 'Животноводство'), ('aviculture', 'Птицеводство'),
    ('pisciculture', 'Рыбоводство'), ('plant_growing', 'Растениеводство'),
    ('apiculture', 'Пчеловодство'), ('stern', 'Корма'),
    ('veterinary_drugs', 'Ветиренарные препараты'), ('the_property', 'Недвижимость'),
    ('production', 'Продукция'), ('equipment', 'Сельхоз техника и оборудование'),
    ('fertilizer', 'Удобрения'))


class CreateNewAdvert(models.Model):
    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'

    name = models.CharField(verbose_name='Name', max_length=255, null=True)
    email = models.CharField(verbose_name='Email', max_length=255, null=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок', null=True)
    media = models.ManyToManyField('Media', verbose_name='Изображения', blank=True)
    advert_type = models.CharField(max_length=255, verbose_name='Тип объявления',
                                   choices=ad_type)
    categories = models.CharField(max_length=255, verbose_name='Категория',
                                  choices=Category_type, )
    text = RichTextUploadingField()
    date = models.DateField("Date", auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Подтверждено')
    agree_with_rules = models.BooleanField(default=False, verbose_name='Согласен с правилами')

    def __unicode__(self):
        # return 'ad object'
        return self.title


class Media(models.Model):
    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'

    media_file = models.FileField(verbose_name='Медиа файл')

    def get_absolute_url(self):
        return self.media_file.url

    def save(self, *args, **kwargs):
        super(Media, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.media_file)
