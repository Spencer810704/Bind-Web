# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-02 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dns_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=5)),
                ('data', models.CharField(blank=True, max_length=255, null=True)),
                ('ttl', models.IntegerField()),
                ('mx_priority', models.IntegerField(blank=True, null=True)),
                ('view', models.CharField(max_length=7)),
                ('priority', models.IntegerField()),
                ('refresh', models.IntegerField()),
                ('retry', models.IntegerField()),
                ('expire', models.IntegerField()),
                ('minimum', models.IntegerField()),
                ('serial', models.BigIntegerField()),
                ('resp_person', models.CharField(max_length=64)),
                ('primary_ns', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'dns_records',
            },
        ),
        migrations.AlterIndexTogether(
            name='dns_record',
            index_together=set([('zone', 'host')]),
        ),
    ]