# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-04 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kwaddle', '0059_auto_20180703_2240'),
        ('blog', '0025_auto_20180702_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostsCompanies',
            fields=[
                ('posts_companies_id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwaddle.Company')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='companies',
            field=models.ManyToManyField(through='blog.PostsCompanies', to='kwaddle.Company'),
        ),
        migrations.AlterUniqueTogether(
            name='postscompanies',
            unique_together=set([('post', 'company')]),
        ),
    ]
