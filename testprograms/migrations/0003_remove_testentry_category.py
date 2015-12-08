# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0002_auto_20150902_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testentry',
            name='category',
        ),
    ]
