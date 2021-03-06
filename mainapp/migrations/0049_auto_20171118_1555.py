# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0048_auto_20171118_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmembership',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Organization'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organizationmembership',
            name='role',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
