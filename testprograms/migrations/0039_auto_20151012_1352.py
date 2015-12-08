# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0038_auto_20151012_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programtutorialcontent',
            name='program_tutorial',
            field=models.ForeignKey(to='testprograms.ProgramTutorial', null=True, related_name='topics'),
        ),
    ]
