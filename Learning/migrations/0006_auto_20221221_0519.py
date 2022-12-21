# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-12-21 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0005_slideimages_game_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='images')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='SlideImages',
        ),
        migrations.AddField(
            model_name='games_type',
            name='slideimages',
            field=models.ManyToManyField(related_name='slideimage', to='Learning.Images'),
        ),
        migrations.AddField(
            model_name='games_type',
            name='splashImg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splashimg', to='Learning.Images'),
        ),
    ]