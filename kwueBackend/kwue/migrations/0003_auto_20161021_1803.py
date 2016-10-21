# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0002_auto_20161015_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='created_date',
            new_name='food_created_date',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='name',
            new_name='food_name',
        ),
        migrations.AddField(
            model_name='food',
            name='food_description',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='food_id',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]
