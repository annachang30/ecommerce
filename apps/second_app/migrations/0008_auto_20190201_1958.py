# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-01 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0007_auto_20190201_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ManyToManyField(related_name='products', to='second_app.Order'),
        ),
    ]
