# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='time',
        ),
    ]
