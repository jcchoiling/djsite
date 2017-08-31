# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
    ]