# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20161019_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almaurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
