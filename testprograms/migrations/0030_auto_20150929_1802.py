# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0029_auto_20150929_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimediacontent',
            name='api_pic_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='multimediacontent',
            name='api_title',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='multimediacontent',
            name='api_view_count',
            field=models.IntegerField(null=True),
        ),
    ]
