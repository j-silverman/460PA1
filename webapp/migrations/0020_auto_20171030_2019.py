# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 00:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_tag_t_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='t_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]