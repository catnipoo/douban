# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-28 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='电影名')),
                ('director', models.CharField(max_length=200, verbose_name='导演')),
                ('screenwriter', models.CharField(max_length=400, verbose_name='编剧')),
                ('starring', models.CharField(max_length=600, verbose_name='主演')),
                ('types', models.CharField(max_length=120, verbose_name='类型')),
                ('area', models.CharField(max_length=20, verbose_name='地区')),
                ('language', models.CharField(max_length=20, verbose_name='语言')),
                ('date', models.CharField(max_length=100, verbose_name='上映日期')),
                ('lengh', models.CharField(max_length=100, verbose_name='片长')),
                ('imdb_href', models.CharField(max_length=200, verbose_name='IMDb链接')),
                ('img_url', models.CharField(max_length=300, verbose_name='图片')),
                ('score', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='评分')),
                ('synopsis', models.TextField(verbose_name='剧情简介')),
            ],
            options={
                'verbose_name': '豆瓣',
                'verbose_name_plural': '豆瓣',
                'db_table': 'tb_douban',
            },
        ),
    ]
