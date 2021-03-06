# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20, blank=True)),
                ('message', models.TextField()),
                ('contact', models.ForeignKey(null=True, to='library.Contact', blank=True)),
            ],
        ),
    ]
