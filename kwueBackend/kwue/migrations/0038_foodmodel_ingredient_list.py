# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0037_auto_20161113_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmodel',
            name='ingredient_list',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]