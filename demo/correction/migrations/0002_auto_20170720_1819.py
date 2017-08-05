# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-20 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('correction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='watcategory',
            name='id',
        ),
        migrations.AddField(
            model_name='watcategory',
            name='category_id',
            field=models.PositiveIntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataneedscorrection',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='correction.WatCategory'),
        ),
    ]
