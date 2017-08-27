# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-27 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_app', '0004_auto_20170827_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_Movie_code', models.CharField(max_length=100)),
                ('movie_title', models.CharField(max_length=50)),
                ('poster_path', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.User')),
            ],
        ),
    ]
