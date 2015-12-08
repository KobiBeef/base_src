# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testprograms', '0013_auto_20150918_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebTheme',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('theme_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('theme_image', models.ImageField(blank=True, upload_to='static/testprograms/images/')),
                ('theme_desc_short', models.TextField()),
                ('theme_desc_long', models.TextField()),
                ('theme_created', models.DateTimeField(auto_now_add=True)),
                ('theme_modified', models.DateTimeField(auto_now=True)),
                ('theme_author', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='theme_author')),
            ],
            options={
                'verbose_name_plural': 'Web Themes',
                'verbose_name': 'Web Theme ',
            },
        ),
        migrations.CreateModel(
            name='WebThemeCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('web_theme_category', models.ForeignKey(to='testprograms.Category', null=True)),
            ],
            options={
                'verbose_name_plural': 'Web Theme Categories',
                'verbose_name': 'Web Theme Category',
            },
        ),
        migrations.CreateModel(
            name='WebThemeFeature',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('feature', models.CharField(unique=True, max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Web Theme Features',
                'verbose_name': 'Web Theme Feature',
            },
        ),
        migrations.CreateModel(
            name='WebThemeType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('web_theme_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Web Theme Types',
                'verbose_name': 'Web Theme Type',
            },
        ),
        migrations.AddField(
            model_name='webtheme',
            name='theme_category',
            field=models.ForeignKey(to='testprograms.WebThemeCategory', null=True),
        ),
        migrations.AddField(
            model_name='webtheme',
            name='theme_features',
            field=models.ManyToManyField(to='testprograms.WebThemeFeature', null=True),
        ),
        migrations.AddField(
            model_name='webtheme',
            name='theme_tags',
            field=models.ManyToManyField(to='testprograms.Tag'),
        ),
        migrations.AddField(
            model_name='webtheme',
            name='theme_type',
            field=models.ForeignKey(to='testprograms.WebThemeType', null=True),
        ),
    ]
