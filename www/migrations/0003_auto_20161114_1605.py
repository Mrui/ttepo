# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20161114_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmember',
            name='photo',
            field=models.ImageField(upload_to='./board/'),
        ),
    ]