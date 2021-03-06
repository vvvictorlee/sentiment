# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-20 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataCorrected',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('correctedText', models.CharField(max_length=300)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DataNeedsCorrection',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('originalText', models.CharField(max_length=300)),
                ('translatedText', models.CharField(max_length=300)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DataValidated',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('referenceData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='correction.DataNeedsCorrection')),
            ],
        ),
        migrations.CreateModel(
            name='WatCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='datacorrected',
            name='referenceData',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='correction.DataNeedsCorrection'),
        ),
    ]
