# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_departmentmembership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='submitter_committee',
            field=models.ManyToManyField(blank=True, to='mainapp.Committee'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submitter_department',
            field=models.ManyToManyField(blank=True, to='mainapp.Department'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submitter_parliamentary_group',
            field=models.ManyToManyField(blank=True, to='mainapp.ParliamentaryGroup'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='submitter_persons',
            field=models.ManyToManyField(blank=True, to='mainapp.Person'),
        ),
    ]
