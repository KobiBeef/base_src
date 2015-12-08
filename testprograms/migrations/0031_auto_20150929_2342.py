# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0030_auto_20150929_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiMediaApi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('api_title', models.CharField(null=True, max_length=500)),
                ('api_pic_count', models.IntegerField(null=True)),
                ('api_view_count', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'MultiMedia API',
                'verbose_name_plural': "MultiMedia API's",
            },
        ),
        migrations.RemoveField(
            model_name='multimediacontent',
            name='api_pic_count',
        ),
        migrations.RemoveField(
            model_name='multimediacontent',
            name='api_title',
        ),
        migrations.RemoveField(
            model_name='multimediacontent',
            name='api_view_count',
        ),
    ]
