# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-16 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_gameslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gameslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=225, unique=True)),
                ('Console', models.CharField(max_length=50, unique=True)),
                ('ReleaseDate', models.CharField(max_length=10, unique=True)),
                ('Description', models.CharField(max_length=5000, unique=True)),
                ('FondMemories', models.CharField(max_length=10000, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
