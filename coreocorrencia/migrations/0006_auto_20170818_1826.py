# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreocorrencia', '0005_posteres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poster',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Poster',
        ),
    ]
