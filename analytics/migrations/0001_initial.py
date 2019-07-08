# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0005_auto_20161020_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('alma_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.AlmaURL')),
            ],
        ),
    ]