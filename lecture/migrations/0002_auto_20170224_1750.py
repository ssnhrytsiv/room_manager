# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-24 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20170211_0248'),
        ('group', '0002_group_captain'),
        ('user', '0002_auto_20170208_1825'),
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='group',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Lesson', to='group.Group'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='number_by_schedule',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lecture',
            name='room',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Lesson', to='room.Room'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='teacher',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Lesson', to='user.User'),
        ),
    ]
