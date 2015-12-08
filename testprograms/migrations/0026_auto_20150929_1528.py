# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0025_webtheme_live_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimediacontent',
            name='api_pic_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='api_title',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='api_view_count',
            field=models.IntegerField(null=True),
        ),
    ]
