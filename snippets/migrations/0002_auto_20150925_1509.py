# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='snippets'),
        ),
    ]