# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0025_auto_20161027_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumptionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='foodmodel',
            name='user_history',
        ),
        migrations.AddField(
            model_name='consumptionhistory',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwue.FoodModel'),
        ),
        migrations.AddField(
            model_name='consumptionhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwue.UserModel'),
        ),
    ]
