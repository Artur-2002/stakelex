# Generated by Django 2.1.5 on 2021-04-28 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0029_auto_20210428_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_KAZ',
            field=models.BooleanField(default=False, verbose_name='Отображать только Казахстанские банки'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_RU',
            field=models.BooleanField(default=False, verbose_name='Отображать только Российские банки'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_UK',
            field=models.BooleanField(default=False, verbose_name='Отображать только Украинские банки'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 19, 4, 40, 78737), verbose_name='Дата и время регистрации'),
        ),
    ]