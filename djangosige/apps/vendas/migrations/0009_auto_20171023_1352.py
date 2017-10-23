# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0008_auto_20171023_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.Cliente'),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='passageiro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.Passageiro'),
        ),
    ]
