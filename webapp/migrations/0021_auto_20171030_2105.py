# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20171030_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Photos'),
        ),
    ]