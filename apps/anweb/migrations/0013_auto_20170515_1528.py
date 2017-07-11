# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anweb', '0012_auto_20170510_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysql',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nginx',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='redis',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tomcat',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]