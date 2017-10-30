# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(blank=True, max_length=20)),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Photos')),
            ],
        ),
    ]