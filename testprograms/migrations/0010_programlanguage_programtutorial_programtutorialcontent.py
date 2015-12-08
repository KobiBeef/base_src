# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0009_auto_20150917_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramLanguage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('language', models.ForeignKey(to='testprograms.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramTutorial',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tutorial_name', models.CharField(max_length=100)),
                ('tutorial_url', models.URLField(max_length=100, blank=True)),
                ('tutorial_desc', models.TextField()),
                ('tutorial_created', models.DateTimeField(auto_now_add=True)),
                ('tutorial_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=100)),
                ('program_language', models.ForeignKey(to='testprograms.ProgramLanguage', null=True)),
                ('tutorial_tags', models.ManyToManyField(to='testprograms.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramTutorialContent',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tutorial_topic', models.CharField(max_length=100)),
                ('tutorial_body', models.TextField()),
                ('tutorial_resources', models.URLField(max_length=100, blank=True)),
                ('program_tutorial', models.ForeignKey(to='testprograms.ProgramTutorial', null=True)),
            ],
        ),
    ]
