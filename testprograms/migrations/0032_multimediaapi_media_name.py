# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0031_auto_20150929_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimediaapi',
            name='media_name',
            field=models.ForeignKey(null=True, to='testprograms.MultiMediaContent'),
        ),
    ]
