# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20150908_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcomment',
            name='contact',
            field=models.ForeignKey(to='library.Contact', blank=True, null=True),
        ),
    ]
