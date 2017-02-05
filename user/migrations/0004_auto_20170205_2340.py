# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_group_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.Group'),
        ),
    ]
