# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-21 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20180621_1821'),
    ]

    operations = [
        # migrations.DeleteModel(
        #     name='PostImageSet',
        # ),
        # migrations.RemoveField(
        #     model_name='post',
        #     name='image_set',
        # ),
        migrations.AlterField(
            model_name='post',
            name='markup',
            field=models.CharField(choices=[('markdown', 'Markdown'), ('html', 'Html')], max_length=25, verbose_name='Markup'),
        ),
    ]
