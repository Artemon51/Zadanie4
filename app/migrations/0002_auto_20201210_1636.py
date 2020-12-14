# Generated by Django 2.2.16 on 2020-12-10 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 16, 36, 3, 550699), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 16, 36, 3, 551697), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 16, 36, 3, 551697), verbose_name='Дата'),
        ),
    ]