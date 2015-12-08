# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0010_programlanguage_programtutorial_programtutorialcontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programlanguage',
            options={'verbose_name_plural': 'Programming Languages', 'verbose_name': 'Programming Language'},
        ),
        migrations.AlterModelOptions(
            name='programtutorial',
            options={'verbose_name_plural': 'Programming Tutorials', 'verbose_name': 'Programming Tutorial'},
        ),
        migrations.AlterModelOptions(
            name='programtutorialcontent',
            options={'verbose_name_plural': 'Programming Tutorial Contents', 'verbose_name': 'Programming Tutorial Content'},
        ),
    ]
