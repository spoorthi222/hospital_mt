# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-03 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20190731_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='salt',
            field=models.CharField(default=b'', max_length=64),
        ),
    ]
