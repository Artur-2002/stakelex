# Generated by Django 2.1.5 on 2021-02-18 10:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20210218_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referals1_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
    ]
