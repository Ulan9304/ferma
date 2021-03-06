# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 12:57
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateNewAdvert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='Email')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('advert_type', models.CharField(choices=[('sell', '\u041f\u0440\u043e\u0434\u0430\u044e'), ('buy', '\u041a\u0443\u043f\u043b\u044e'), ('change', '\u041c\u0435\u043d\u044f\u044e'), ('rent', '\u0410\u0440\u0435\u043d\u0434\u0430'), ('offers', '\u0423\u0441\u043b\u0443\u0433\u0438')], max_length=255, verbose_name='\u0422\u0438\u043f \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('categories', models.CharField(choices=[('stock_raising', '\u0416\u0438\u0432\u043e\u0442\u043d\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e'), ('aviculture', '\u041f\u0442\u0438\u0446\u0435\u0432\u043e\u0434\u0441\u0442\u0432\u043e'), ('pisciculture', '\u0420\u044b\u0431\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e'), ('plant_growing', '\u0420\u0430\u0441\u0442\u0435\u043d\u0438\u0435\u0432\u043e\u0434\u0441\u0442\u0432\u043e'), ('apiculture', '\u041f\u0447\u0435\u043b\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e'), ('stern', '\u041a\u043e\u0440\u043c\u0430'), ('veterinary_drugs', '\u0412\u0435\u0442\u0438\u0440\u0435\u043d\u0430\u0440\u043d\u044b\u0435 \u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u044b'), ('the_property', '\u041d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c'), ('production', '\u041f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u044f'), ('equipment', '\u0421\u0435\u043b\u044c\u0445\u043e\u0437 \u0442\u0435\u0445\u043d\u0438\u043a\u0430 \u0438 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435'), ('fertilizer', '\u0423\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f')], max_length=255, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateField(auto_now_add=True, null=True, verbose_name='Date')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043e')),
                ('agree_with_rules', models.BooleanField(default=False, verbose_name='\u0421\u043e\u0433\u043b\u0430\u0441\u0435\u043d \u0441 \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c\u0438')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(upload_to=b'', verbose_name='\u041c\u0435\u0434\u0438\u0430 \u0444\u0430\u0439\u043b')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0434\u0438\u0430',
                'verbose_name_plural': '\u041c\u0435\u0434\u0438\u0430',
            },
        ),
        migrations.AddField(
            model_name='createnewadvert',
            name='media',
            field=models.ManyToManyField(blank=True, to='adverts.Media', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f'),
        ),
    ]
