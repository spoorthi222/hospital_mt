# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-24 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='N/A', max_length=50)),
                ('desig', models.CharField(max_length=40)),
                ('s_scale', models.CharField(default='N/A', max_length=7)),
            ],
            options={
                'db_table': 'staff_table_1',
            },
        ),
    ]
