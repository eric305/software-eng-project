# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_techvalleytimes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amount_sold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
