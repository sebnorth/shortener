# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20160614_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='submitter',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
