# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-26 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0015_auto_20171026_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='passageiro',
            name='telefone_responsavel',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
