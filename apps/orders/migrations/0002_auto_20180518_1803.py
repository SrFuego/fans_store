# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-18 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False, verbose_name='entregado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='model',
            field=models.ManyToManyField(to='products.Model', verbose_name='modelos'),
        ),
        migrations.AlterField(
            model_name='order',
            name='mount',
            field=models.PositiveSmallIntegerField(verbose_name='total'),
        ),
    ]
