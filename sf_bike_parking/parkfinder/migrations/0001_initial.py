# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeParking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('locationName', models.CharField(max_length=200)),
                ('streetName', models.CharField(max_length=200)),
                ('racks', models.IntegerField()),
                ('spaces', models.IntegerField()),
                ('placement', models.CharField(max_length=10)),
                ('monthInstalled', models.IntegerField()),
                ('yearInstalled', models.IntegerField()),
                ('coordinates', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
