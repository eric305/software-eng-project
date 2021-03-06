# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 15:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_book_release_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0018_auto_20170703_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='FutureOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'future_orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FutureOrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='future_book', to='products.Book')),
                ('future_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.FutureOrder')),
            ],
            options={
                'db_table': 'future_order_items',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='products.Book'),
        ),
    ]
