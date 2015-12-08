# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0035_auto_20151012_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='num_comment',
            new_name='comment',
        ),
    ]
