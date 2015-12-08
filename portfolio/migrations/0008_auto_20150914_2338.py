# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20150912_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebTheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('theme_name', models.CharField(max_length=50)),
                ('theme_image', models.ImageField(blank=True, upload_to='test_images')),
                ('theme_slug', models.SlugField(unique=True, max_length=200)),
                ('theme_desc_short', models.TextField()),
                ('theme_desc_long', models.TextField()),
                ('theme_author', models.CharField(max_length=50)),
                ('theme_license', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('theme_category', models.ForeignKey(null=True, to='portfolio.Category')),
            ],
            options={
                'verbose_name': 'Web Theme',
                'verbose_name_plural': 'Web Themes',
            },
        ),
        migrations.CreateModel(
            name='WebThemeFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('feature', models.CharField(unique=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Web Theme Feature',
                'verbose_name_plural': 'Web Theme Features',
            },
        ),
        migrations.AddField(
            model_name='webtheme',
            name='theme_features',
            field=models.ManyToManyField(to='portfolio.WebThemeFeature'),
        ),
        migrations.AddField(
            model_name='webtheme',
            name='theme_tags',
            field=models.ManyToManyField(to='portfolio.Tag'),
        ),
    ]
