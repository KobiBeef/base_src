# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0037_auto_20151012_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwarecomment',
            name='hardware_comment_post',
            field=models.ForeignKey(null=True, to='testprograms.HardwarePost', related_name='comments'),
        ),
    ]
