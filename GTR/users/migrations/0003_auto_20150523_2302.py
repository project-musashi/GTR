# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150523_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='link',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voter',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
