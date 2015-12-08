# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='modifield',
        ),
    ]
