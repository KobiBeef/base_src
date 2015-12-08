# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0033_auto_20150929_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimediacontent',
            name='url',
            field=models.URLField(max_length=100, blank=True),
        ),
    ]
