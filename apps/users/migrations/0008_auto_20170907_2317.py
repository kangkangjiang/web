# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170902_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birday',
            field=models.CharField(max_length=64, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(default=0, max_length=12, verbose_name='用户电话'),
        ),
    ]
