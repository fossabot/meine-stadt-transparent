# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0036_auto_20171030_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendaitem',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='papertype',
            name='paper_type',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
