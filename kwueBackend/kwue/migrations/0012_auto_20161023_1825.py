# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0011_auto_20161023_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='owner_id',
            new_name='commented_object_id',
        ),
        migrations.RemoveField(
            model_name='commentmodel',
            name='commented_food',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='comment_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kwue.UserModel'),
            preserve_default=False,
        ),
    ]