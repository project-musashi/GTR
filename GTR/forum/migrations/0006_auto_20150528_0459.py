# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_link_self_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='self_description',
            field=models.TextField(blank=True, verbose_name='Self description'),
        ),
    ]
