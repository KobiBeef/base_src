# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20150914_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webtheme',
            old_name='theme_slug',
            new_name='slug',
        ),
    ]
