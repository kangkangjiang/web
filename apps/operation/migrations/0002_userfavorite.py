# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 15:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='用户名字')),
                ('favid', models.IntegerField(default=0, max_length=50, verbose_name='数据ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('fa_type', models.CharField(choices=[(1, '课程'), (2, '讲师'), (3, '机构')], max_length=50)),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
    ]