# Generated by Django 2.1.5 on 2021-02-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20210217_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referal1_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уникальный номер первого реферала'),
        ),
        migrations.AddField(
            model_name='profile',
            name='referal2_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уникальный номер второго реферала'),
        ),
        migrations.AddField(
            model_name='profile',
            name='referal3_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уникальный номер третьего реферала'),
        ),
        migrations.AddField(
            model_name='profile',
            name='referal4_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уникальный номер четвертого реферала'),
        ),
    ]