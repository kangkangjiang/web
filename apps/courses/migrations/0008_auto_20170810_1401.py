# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20170810_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='clik_nums',
            field=models.IntegerField(verbose_name='点击数'),
        ),
    ]