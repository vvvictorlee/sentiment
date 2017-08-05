# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-20 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mainmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('path', models.CharField(max_length=30)),
            ],
        ),
    ]
