# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0034_auto_20171030_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='paper_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.PaperType'),
        ),
    ]
