# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('usage_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'get_latest_by': 'date_submitted',
            },
        ),
    ]
