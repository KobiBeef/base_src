# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_programtutorial_programtutorialdetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programtutorialdetail',
            options={'verbose_name_plural': 'Program Tutorial Details', 'verbose_name': 'Program Tutorial Detail'},
        ),
    ]
