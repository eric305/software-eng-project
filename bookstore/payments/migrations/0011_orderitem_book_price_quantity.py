# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_auto_20170622_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='book_price_quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
