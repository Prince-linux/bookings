# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_of_booking', models.CharField(max_length=30)),
                ('price_of_booking', models.CharField(max_length=30)),
                ('available', models.BooleanField()),
            ],
        ),
    ]
