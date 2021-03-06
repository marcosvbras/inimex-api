# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-17 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.IntegerField(default=0)),
                ('status', models.IntegerField(blank=True, choices=[('1', 'Watching'), ('2', 'Completed'), ('3', 'Dropped'), ('4', 'Plan To Watch')], null=True)),
                ('rate', models.IntegerField(blank=True, choices=[('1', 'Appalling'), ('2', 'Horrible'), ('3', 'Very Bad'), ('4', 'Bad'), ('5', 'Average'), ('6', 'Fine'), ('7', 'Good'), ('8', 'Very Good'), ('9', 'Great'), ('10', 'Masterpiece')], null=True)),
                ('start_watch_date', models.DateTimeField(blank=True, null=True)),
                ('finish_watch_date', models.DateTimeField(blank=True, null=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.Anime')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
