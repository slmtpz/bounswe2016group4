# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0023_auto_20161027_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='comment_parent',
            new_name='parent',
        ),
    ]