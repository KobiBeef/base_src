# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0027_remove_multimediacontent_api_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimediacontent',
            name='api_title',
            field=models.CharField(null=True, max_length=500),
        ),
    ]
