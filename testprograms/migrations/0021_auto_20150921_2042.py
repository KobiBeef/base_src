# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0020_auto_20150921_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Entries', 'verbose_name': 'Entry'},
        ),
        migrations.AlterModelOptions(
            name='hardwarepost',
            options={'ordering': ['-hardware_post_created'], 'verbose_name_plural': 'Hardware Posts', 'verbose_name': 'Hardware Post'},
        ),
    ]
