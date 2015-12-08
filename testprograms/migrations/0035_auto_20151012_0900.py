# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0034_multimediacontent_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrycomment',
            name='post',
        ),
        migrations.AddField(
            model_name='entry',
            name='num_comment',
            field=models.ForeignKey(null=True, to='testprograms.EntryComment'),
        ),
    ]
