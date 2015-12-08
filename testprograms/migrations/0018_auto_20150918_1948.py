# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0017_auto_20150918_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hardwarecomment',
            options={'verbose_name_plural': 'Hardware Comments', 'verbose_name': 'Hardware Comment'},
        ),
    ]
