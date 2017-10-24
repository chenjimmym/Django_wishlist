# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='wished_by',
            field=models.ManyToManyField(related_name='items_wished', to='wishlist.User'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='added_by',
        ),
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items_added', to='wishlist.User'),
            preserve_default=False,
        ),
    ]
