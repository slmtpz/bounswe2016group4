# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kwue', '0040_auto_20161113_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodSerModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='food_rate_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='allergic_ingredients',
            field=models.ManyToManyField(to='kwue.IngredientModel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='calorie_lower_bound',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='calorie_upper_bound',
            field=models.FloatField(default=10000),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='carbohydrate_lower_bound',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='carbohydrate_upper_bound',
            field=models.FloatField(default=100000),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='fat_lower_bound',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='fat_upper_bound',
            field=models.FloatField(default=100000),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='preference_tags',
            field=models.ManyToManyField(to='kwue.TagModel'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='protein_lower_bound',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='protein_upper_bound',
            field=models.FloatField(default=1000),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='sugar_lower_bound',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='sugar_upper_bound',
            field=models.FloatField(default=10000),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='food_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwue.FoodSerModel'),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='food_rate',
            field=models.FloatField(default=0),
        ),
    ]
