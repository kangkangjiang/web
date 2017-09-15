# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgnization', '0011_auto_20170808_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='org/%Y/%M', verbose_name='教师照片'),
        ),
        migrations.AlterField(
            model_name='orgcate',
            name='name',
            field=models.CharField(max_length=50, verbose_name='机构类别'),
        ),
    ]