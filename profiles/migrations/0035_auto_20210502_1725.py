# Generated by Django 2.1.5 on 2021-05-02 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_auto_20210502_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 17, 25, 29, 623473), verbose_name='Дата и время регистрации'),
        ),
    ]