# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 22:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
    ]
