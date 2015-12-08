# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0007_auto_20150916_1259'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestEntry',
            new_name='Entry',
        ),
        migrations.RenameModel(
            old_name='TestEntryComment',
            new_name='EntryComment',
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries', 'verbose_name': 'Entry'},
        ),
        migrations.AlterModelOptions(
            name='entrycomment',
            options={'verbose_name_plural': 'Entry Comments', 'verbose_name': 'Entry Comment'},
        ),
    ]
