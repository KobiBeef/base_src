# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0024_auto_20150923_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='webtheme',
            name='live_preview',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
