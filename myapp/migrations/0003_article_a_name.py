# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='a_name',
            field=models.CharField(default='machine learning', max_length=50),
        ),
    ]
