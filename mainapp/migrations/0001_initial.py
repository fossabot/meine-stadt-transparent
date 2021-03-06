# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20)),
                ('position', models.IntegerField()),
                ('public', models.NullBooleanField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommitteeMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('role', models.CharField(max_length=200)),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Committee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('storage_filename', models.CharField(max_length=256)),
                ('displayed_filename', models.CharField(max_length=256)),
                ('legal_date', models.DateField()),
                ('filesize', models.IntegerField()),
                ('parsed_text', models.TextField(blank=True, null=True)),
                ('license', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegislativeTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('displayed_name', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_official', models.BooleanField()),
                ('osm_id', models.BigIntegerField(blank=True, null=True)),
                ('geometry', djgeojson.fields.GeometryField(default=None)),
                ('bodies', models.ManyToManyField(blank=True, to='mainapp.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000)),
                ('cancelled', models.BooleanField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('public', models.IntegerField(blank=True, choices=[(0, 'unknown'), (1, 'public'), (2, 'not public'), (3, 'splitted')], default=0)),
                ('auxiliary_files', models.ManyToManyField(blank=True, related_name='meeting_auxiliary_files', to='mainapp.File')),
                ('committees', models.ManyToManyField(blank=True, to='mainapp.Committee')),
                ('invitation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_invitation', to='mainapp.File')),
                ('locations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_regular', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('reference_number', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_change_request_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Paper')),
                ('submitter_committee', models.ManyToManyField(to='mainapp.Committee')),
                ('submitter_department', models.ManyToManyField(to='mainapp.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParliamentaryGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('short_name', models.CharField(max_length=20)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Body')),
                ('legislative_terms', models.ManyToManyField(blank=True, to='mainapp.LegislativeTerm')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParliamentaryGroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('role', models.CharField(max_length=200)),
                ('parliamentary_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ParliamentaryGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('given_name', models.CharField(max_length=50)),
                ('family_name', models.CharField(max_length=50)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SearchPoi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('displayed_name', models.CharField(max_length=1000)),
                ('osm_id', models.BigIntegerField(blank=True, null=True)),
                ('osm_amenity', models.CharField(max_length=1000, null=True)),
                ('geometry', djgeojson.fields.GeometryField(null=True)),
                ('exclude_from_search', models.BooleanField(default=False)),
                ('bodies', models.ManyToManyField(blank=True, to='mainapp.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SearchStreet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oparl_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('displayed_name', models.CharField(max_length=1000)),
                ('osm_id', models.BigIntegerField(blank=True, null=True)),
                ('exclude_from_search', models.BooleanField(default=False)),
                ('bodies', models.ManyToManyField(blank=True, to='mainapp.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='parliamentarygroupmembership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Person'),
        ),
        migrations.AddField(
            model_name='paper',
            name='submitter_parliamentary_group',
            field=models.ManyToManyField(to='mainapp.ParliamentaryGroup'),
        ),
        migrations.AddField(
            model_name='paper',
            name='submitter_persons',
            field=models.ManyToManyField(to='mainapp.Person'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.MeetingSeries'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='persons',
            field=models.ManyToManyField(blank=True, to='mainapp.Person'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='results_protocol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_results_protocol', to='mainapp.File'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='verbatim_protocol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_verbatim_protocol', to='mainapp.File'),
        ),
        migrations.AddField(
            model_name='file',
            name='locations',
            field=models.ManyToManyField(blank=True, to='mainapp.Location'),
        ),
        migrations.AddField(
            model_name='file',
            name='paper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Paper'),
        ),
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Location'),
        ),
        migrations.AddField(
            model_name='committeemembership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Person'),
        ),
        migrations.AddField(
            model_name='committee',
            name='legislative_terms',
            field=models.ManyToManyField(blank=True, to='mainapp.LegislativeTerm'),
        ),
        migrations.AddField(
            model_name='committee',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Location'),
        ),
        migrations.AddField(
            model_name='body',
            name='center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='body_center', to='mainapp.Location'),
        ),
        migrations.AddField(
            model_name='body',
            name='legislative_terms',
            field=models.ManyToManyField(to='mainapp.LegislativeTerm'),
        ),
        migrations.AddField(
            model_name='body',
            name='outline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='body_outline', to='mainapp.Location'),
        ),
        migrations.AddField(
            model_name='agendaitem',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Meeting'),
        ),
        migrations.AddField(
            model_name='agendaitem',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Paper'),
        ),
        migrations.AlterUniqueTogether(
            name='agendaitem',
            unique_together=set([('meeting', 'position')]),
        ),
    ]
