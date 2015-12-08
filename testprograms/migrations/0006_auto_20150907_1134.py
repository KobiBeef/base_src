# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0005_testentrycomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testentrycomment',
            options={'verbose_name_plural': 'Test Entry Comments', 'verbose_name': 'Test Entry Comment'},
        ),
    ]
