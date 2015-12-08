# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0016_auto_20150918_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hardwarefeature',
            options={'verbose_name': 'Hardware Feature', 'verbose_name_plural': 'Hardware Features'},
        ),
    ]
