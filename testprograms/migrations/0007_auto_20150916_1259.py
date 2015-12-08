# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0006_auto_20150907_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testentrycomment',
            name='post',
            field=models.ForeignKey(to='testprograms.TestEntry', blank=True, null=True),
        ),
    ]
