# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170830_0345'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('slug', 'course')]),
        ),
    ]
