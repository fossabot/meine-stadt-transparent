# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_auto_20171030_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='reference_number',
            field=models.CharField(default='[Deleted]', max_length=50),
            preserve_default=False,
        ),
    ]