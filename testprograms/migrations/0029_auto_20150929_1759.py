# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0028_multimediacontent_api_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimediacontent',
            name='api_pic_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='multimediacontent',
            name='api_title',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='multimediacontent',
            name='api_view_count',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
