# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-28 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'', max_length=50)),
                ('email_id', models.CharField(default=b'', max_length=100)),
                ('phone_no', models.CharField(default=b'', max_length=7)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
