# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0011_auto_20150917_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programtutorial',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
