# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0032_multimediaapi_media_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimediaapi',
            name='media_name',
        ),
        migrations.AddField(
            model_name='multimediacontent',
            name='api',
            field=models.ForeignKey(null=True, to='testprograms.MultiMediaApi'),
        ),
    ]
