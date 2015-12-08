# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0018_auto_20150918_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hardwarecategory',
            old_name='hardware_category',
            new_name='category',
        ),
    ]
