# Generated by Django 2.1 on 2018-08-23 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 17, 13, 22, 285834), verbose_name='添加时间'),
        ),
    ]