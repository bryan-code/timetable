# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20170831_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='time',
            field=models.TimeField(),
        ),
    ]
