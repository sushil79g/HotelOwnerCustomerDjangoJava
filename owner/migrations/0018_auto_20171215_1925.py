# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0017_auto_20171212_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='token',
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='specialitysignup',
            name='signup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Signup'),
        ),
        migrations.AlterField(
            model_name='ssidsignup',
            name='signup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Signup'),
        ),
    ]
