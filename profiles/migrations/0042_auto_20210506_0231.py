# Generated by Django 2.1.5 on 2021-05-05 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0041_auto_20210506_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 2, 31, 59, 590185), verbose_name='Дата и время регистрации'),
        ),
    ]
