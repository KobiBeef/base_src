# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0022_multimediacontent_embed_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimediacontent',
            name='embed_link',
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_condition',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_img_alt',
            field=models.CharField(null=True, max_length=500),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_img_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_img_src',
            field=models.CharField(null=True, max_length=500),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_img_width',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_location',
            field=models.CharField(null=True, max_length=500),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_title',
            field=models.CharField(null=True, max_length=500),
        ),
    ]
