# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20150525_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='disagree',
            field=models.IntegerField(default=0),
        ),
    ]
