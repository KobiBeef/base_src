# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0014_auto_20150918_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtheme',
            name='theme_features',
            field=models.ManyToManyField(to='testprograms.WebThemeFeature'),
        ),
    ]
