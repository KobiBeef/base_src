# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0005_comment_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tutorial_name', models.CharField(max_length=90)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='portfolio.Category', null=True)),
                ('tags', models.ManyToManyField(to='portfolio.Tag')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Program Tutorial',
                'verbose_name_plural': 'Program Tutorials',
            },
        ),
        migrations.CreateModel(
            name='ProgramTutorialDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=90)),
                ('body', models.TextField()),
                ('category', models.ForeignKey(to='portfolio.Category', null=True)),
                ('tutorial_name', models.ForeignKey(to='portfolio.ProgramTutorial', null=True)),
            ],
        ),
    ]
