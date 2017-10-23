# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20170820_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='forma',
            field=models.CharField(choices=[('01', 'Dinheiro'), ('02', 'Cheque'), ('03', 'Cartão de Crédito'), ('04', 'Cartão de Débito'), ('05', 'Crédito Loja')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='condicaopagamento',
            name='forma',
            field=models.CharField(choices=[('01', 'Dinheiro'), ('02', 'Cheque'), ('03', 'Cartão de Crédito'), ('04', 'Cartão de Débito'), ('05', 'Crédito Loja')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='venda',
            name='movimentar_estoque',
            field=models.BooleanField(default=False),
        ),
    ]
