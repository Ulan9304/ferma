# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 11:11
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_auto_20171201_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createnewadvert',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
