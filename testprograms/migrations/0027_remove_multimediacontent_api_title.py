# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0026_auto_20150929_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimediacontent',
            name='api_title',
        ),
    ]
