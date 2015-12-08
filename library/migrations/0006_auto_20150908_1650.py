# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20150908_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcomment',
            name='contact',
            field=models.ForeignKey(to='library.Contact', null=True),
        ),
    ]
