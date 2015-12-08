# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0036_auto_20151012_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='comment',
        ),
        migrations.AddField(
            model_name='entrycomment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='testprograms.Entry', null=True),
        ),
    ]
