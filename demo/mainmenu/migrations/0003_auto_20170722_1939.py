# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-22 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0002_mainmenu_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainmenu',
            options={'ordering': ['-order']},
        ),
    ]