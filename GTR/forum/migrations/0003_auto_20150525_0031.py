# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_link_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='likes',
            new_name='agree',
        ),
    ]
