# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='title', max_length=256),
            preserve_default=False,
        ),
    ]