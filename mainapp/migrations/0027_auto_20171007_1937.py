# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20171007_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='paper',
        ),
        migrations.AddField(
            model_name='agendaitem',
            name='oparl_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='files',
            field=models.ManyToManyField(blank=True, to='mainapp.File'),
        ),
    ]
