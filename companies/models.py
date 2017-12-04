# coding=utf-8
from __future__ import unicode_literals

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Companies(models.Model):
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    image = models.ImageField(verbose_name='Логотип комании', upload_to='company_logo')
    title = models.CharField(verbose_name='Название компании', max_length=255)
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    text = RichTextUploadingField()

    def __unicode__(self):
        return self.title
