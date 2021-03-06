# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='displayed_name',
        ),
        migrations.AddField(
            model_name='legislativeterm',
            name='short_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='short_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='short_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='body',
            name='legislative_terms',
            field=models.ManyToManyField(blank=True, to='mainapp.LegislativeTerm'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='parliamentarygroup',
            name='short_name',
            field=models.CharField(max_length=50),
        ),
    ]
