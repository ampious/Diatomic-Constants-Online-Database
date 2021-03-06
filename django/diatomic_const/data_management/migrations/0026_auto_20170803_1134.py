# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0025_auto_20170803_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diatomic_constant',
            name='delta_minus',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='diatomic_constant',
            name='delta_plus',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='diatomic_constant',
            name='value',
            field=models.FloatField(),
        ),
    ]
