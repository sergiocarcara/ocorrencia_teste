# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 22:23
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coreocorrencia', '0004_poster_polit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fonte', models.CharField(max_length=200)),
                ('imagen', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='')),
                ('texto1', models.TextField(max_length=1000, verbose_name='Primeiro Parágrafo')),
                ('texto2', models.TextField(max_length=1000, verbose_name='Segundo Parágrafo')),
                ('texto3', models.TextField(max_length=1000, verbose_name='Terceiro Parágrafo')),
                ('texto4', models.TextField(max_length=1000, verbose_name='Quarto Parágrafo')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Criação')),
                ('data_publicacao', models.DateTimeField(blank=True, null=True, verbose_name='Data de Publicação')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
