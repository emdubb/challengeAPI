# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('profile_url', models.ImageField(upload_to=None)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]