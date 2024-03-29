# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-26 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastro', '0014_passageiro_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='passageiro',
            name='data_validade_passaporte',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='emissor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='natularidade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='numero_passaporte',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='observacao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='responsavel',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
