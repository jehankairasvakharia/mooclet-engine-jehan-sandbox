# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 08:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0010_auto_20180320_0809'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('mooclet', 'name')]),
        ),
    ]