# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0003_remove_testentry_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='testentry',
            name='category',
            field=models.ForeignKey(to='testprograms.Category', default=''),
            preserve_default=False,
        ),
    ]
