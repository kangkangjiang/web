# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_addcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fa_type',
            field=models.IntegerField(choices=[(1, '课程'), (2, '讲师'), (3, '机构')], default=1, max_length=50),
        ),
    ]