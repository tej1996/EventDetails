# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20161212_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='password1',
            new_name='password',
        ),
    ]
