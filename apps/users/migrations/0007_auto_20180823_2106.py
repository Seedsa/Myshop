# Generated by Django 2.0.7 on 2018-08-23 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180823_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 6, 16, 102124), verbose_name='添加时间'),
        ),
    ]
