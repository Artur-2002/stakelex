# Generated by Django 2.1.5 on 2021-04-28 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0025_profile_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 14, 45, 36, 95399), verbose_name='Дата и время регистрации'),
        ),
    ]
