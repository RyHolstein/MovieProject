# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-26 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0003_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='User_app.User')),
                ('users', models.ManyToManyField(related_name='friend_set', to='User_app.User')),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='api_Movie_code',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imgUrl',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
    ]
