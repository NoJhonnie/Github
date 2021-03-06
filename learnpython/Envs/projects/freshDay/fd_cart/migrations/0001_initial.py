# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fd_goods', '0001_initial'),
        ('fd_user', '0002_auto_20180124_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='fd_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='fd_user.UserInfo')),
            ],
        ),
    ]
