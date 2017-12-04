# coding=utf-8
from __future__ import unicode_literals

# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    preview = models.ImageField(upload_to='news_images/', verbose_name='Превью новости', null=True,
                                blank=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    text = RichTextUploadingField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title
