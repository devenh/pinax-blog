# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-20 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_images', '0001_initial'),
        ('kwaddle', '0052_sort_by_no_blanks'),
        ('blog', '0020_auto_20171106_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImageSet',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('pinax_images.imageset',),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='kwaddle.Category'),
        ),
    ]
