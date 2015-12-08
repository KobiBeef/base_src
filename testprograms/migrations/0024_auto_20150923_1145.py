# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0023_auto_20150923_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimediacontent',
            name='embed_condition',
            field=models.BooleanField(default=False),
        ),
    ]
