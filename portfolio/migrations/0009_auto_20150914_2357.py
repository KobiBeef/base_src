# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20150914_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtheme',
            name='theme_image',
            field=models.ImageField(blank=True, upload_to='static/portfolio/images'),
        ),
    ]
