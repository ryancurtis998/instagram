# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follows',
            name='follower',
        ),
        migrations.DeleteModel(
            name='Follows',
        ),
    ]
