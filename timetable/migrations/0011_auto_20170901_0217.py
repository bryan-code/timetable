# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0010_auto_20170901_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.Event'),
        ),
    ]
