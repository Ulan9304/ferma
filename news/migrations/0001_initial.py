# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 08:20
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='\u041f\u0440\u0435\u0432\u044c\u044e \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
    ]