# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testprograms', '0004_testentry_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestEntryComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(related_name='comments', to='testprograms.TestEntry', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'verbose_name': 'Comment',
            },
        ),
    ]
