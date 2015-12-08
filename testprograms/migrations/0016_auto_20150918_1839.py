# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testprograms', '0015_auto_20150918_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardwareCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('hardware_category', models.ForeignKey(to='testprograms.Category', null=True)),
            ],
            options={
                'verbose_name': 'Hardware Category',
                'verbose_name_plural': 'Hardware Categories',
            },
        ),
        migrations.CreateModel(
            name='HardwareComment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': 'Hardware Post',
                'verbose_name_plural': 'Hardware Posts',
            },
        ),
        migrations.CreateModel(
            name='HardwareDetail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('hardware_name', models.CharField(max_length=200)),
                ('hardware_brand', models.CharField(max_length=100)),
                ('hardware_model', models.CharField(max_length=100)),
                ('hardware_desc', models.TextField()),
                ('hardware_category', models.ForeignKey(to='testprograms.HardwareCategory')),
            ],
            options={
                'verbose_name': 'Hardware Detail',
                'verbose_name_plural': 'Hardware Details',
            },
        ),
        migrations.CreateModel(
            name='HardwareFeature',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('hardware_feature', models.CharField(unique=True, max_length=400)),
            ],
            options={
                'verbose_name': 'Hardware Category',
                'verbose_name_plural': 'Hardware Categories',
            },
        ),
        migrations.CreateModel(
            name='HardwarePost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('hardware_post_title', models.CharField(max_length=100)),
                ('hardware_post_created', models.DateTimeField(auto_now_add=True)),
                ('hardware_post_modified', models.DateTimeField(auto_now=True)),
                ('hardware_post_body', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('hardware_name', models.ForeignKey(to='testprograms.HardwareDetail', null=True)),
                ('hardware_post_creator', models.ForeignKey(related_name='testuserhardware', to=settings.AUTH_USER_MODEL, null=True)),
                ('hardware_post_tags', models.ManyToManyField(to='testprograms.Tag')),
            ],
            options={
                'verbose_name': 'Hardware Post',
                'verbose_name_plural': 'Hardware Posts',
            },
        ),
        migrations.CreateModel(
            name='MultiMediaCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('media_category', models.ForeignKey(to='testprograms.Category', null=True)),
            ],
            options={
                'verbose_name': 'Multimedia Category',
                'verbose_name_plural': 'Multimedia Categories',
            },
        ),
        migrations.CreateModel(
            name='MultiMediaContent',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('media_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('media_created', models.DateTimeField(auto_now_add=True)),
                ('media_path', models.ImageField(upload_to='static/testprograms/images/multimedia/', blank=True)),
                ('media_desc', models.TextField()),
                ('media_category', models.ForeignKey(to='testprograms.MultiMediaCategory', null=True)),
                ('media_creator', models.ForeignKey(related_name='mediatestuser', to=settings.AUTH_USER_MODEL, null=True)),
                ('media_tags', models.ManyToManyField(to='testprograms.Tag')),
            ],
            options={
                'verbose_name': 'Multimedia Content',
                'verbose_name_plural': 'Multimedia Contents',
            },
        ),
        migrations.CreateModel(
            name='MultiMediaType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('media_type', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Multimedia Type',
                'verbose_name_plural': 'Multimedia Types',
            },
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='media_type',
            field=models.ForeignKey(to='testprograms.MultiMediaType', null=True),
        ),
        migrations.AddField(
            model_name='hardwaredetail',
            name='hardware_features',
            field=models.ManyToManyField(to='testprograms.HardwareFeature'),
        ),
        migrations.AddField(
            model_name='hardwarecomment',
            name='hardware_comment_post',
            field=models.ForeignKey(to='testprograms.HardwarePost', null=True),
        ),
    ]
