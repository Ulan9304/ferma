# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 08:20
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createnewadvert',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
