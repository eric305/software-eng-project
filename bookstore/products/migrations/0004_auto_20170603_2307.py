# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170603_2300'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='techvalleytime',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='TechValleyTime',
        ),
    ]