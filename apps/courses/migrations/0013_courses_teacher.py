# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgnization', '0013_auto_20170811_0947'),
        ('courses', '0012_auto_20170828_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgnization.Teacher'),
        ),
    ]