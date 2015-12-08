# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20150915_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtheme',
            name='theme_image',
            field=models.ImageField(blank=True, upload_to='static/portfolio/images/'),
        ),
    ]
