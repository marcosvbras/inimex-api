# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('original_id', models.IntegerField()),
                ('english_title', models.CharField(blank=True, max_length=255, null=True)),
                ('original_title', models.CharField(blank=True, max_length=255, null=True)),
                ('canonical_title', models.CharField(blank=True, max_length=255, null=True)),
                ('season_number', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('air_date', models.CharField(blank=True, max_length=30, null=True)),
                ('thumbnail_url', models.TextField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.Anime')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
