# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('home_town', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
                ('password', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
