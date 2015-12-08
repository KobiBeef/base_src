# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0021_auto_20150921_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimediacontent',
            name='embed_link',
            field=models.TextField(blank=True),
        ),
    ]
