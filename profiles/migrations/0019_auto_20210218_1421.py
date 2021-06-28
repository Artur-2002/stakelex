# Generated by Django 2.1.5 on 2021-02-18 11:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20210218_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referals2_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Номера рефералов в 2 линии'), blank=True, default=[], null=True, size=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='referals3_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Номера рефералов в 3 линии'), blank=True, default=[], null=True, size=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='referals4_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Номера рефералов в 4 линии'), blank=True, default=[], null=True, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='referals1_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Номера рефералов в 1 линии'), blank=True, default=[], null=True, size=None),
        ),
    ]
