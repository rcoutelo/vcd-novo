# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 16:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0009_auto_20171023_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatoprospect',
            name='emissor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
