# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-12 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_remove_lesson_timeout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]