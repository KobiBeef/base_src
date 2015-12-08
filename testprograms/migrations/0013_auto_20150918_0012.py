# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0012_auto_20150917_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrycomment',
            name='post',
            field=models.ForeignKey(null=True, to='testprograms.Entry'),
        ),
    ]
