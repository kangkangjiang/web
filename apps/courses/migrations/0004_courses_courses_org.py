# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgnization', '0011_auto_20170808_0845'),
        ('courses', '0003_auto_20170805_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='courses_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgnization.CourseOrg'),
        ),
    ]
