# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0029_consumptionhistory_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumptionhistory',
            old_name='id',
            new_name='history_id',
        ),
    ]