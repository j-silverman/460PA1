# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20171028_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='album_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Album'),
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='album',
            name='photo_id',
        ),
    ]