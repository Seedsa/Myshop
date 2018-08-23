# Generated by Django 2.1 on 2018-08-23 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180823_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 17, 55, 44, 30273), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 17, 55, 44, 28266), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 17, 55, 44, 27303), help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.CharField(choices=[(2, '二级类目'), (3, '三级类目'), (1, '一级类目')], help_text='类目级别', max_length=20, verbose_name='类目级别'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 17, 55, 44, 28266), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 17, 55, 44, 29269), verbose_name='添加时间'),
        ),
    ]
