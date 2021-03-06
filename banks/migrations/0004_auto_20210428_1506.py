# Generated by Django 2.1.5 on 2021-04-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0003_auto_20210428_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Номер приоритета в списке категории'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='number_all',
            field=models.IntegerField(default=0, verbose_name='Номер приоритета в общем списке'),
        ),
    ]
