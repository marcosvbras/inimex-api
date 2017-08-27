# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('original_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('nsfw', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
