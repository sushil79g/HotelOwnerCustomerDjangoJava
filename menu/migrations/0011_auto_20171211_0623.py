# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20171129_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todayspecial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
