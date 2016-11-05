# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0003_auto_20161022_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followermodel',
            name='food_list_id',
        ),
        migrations.AddField(
            model_name='listmodel',
            name='list_food',
            field=models.ManyToManyField(related_name='foods', to='kwue.FoodModel'),
        ),
        migrations.DeleteModel(
            name='FollowerModel',
        ),
    ]