# Generated by Django 2.1.5 on 2021-04-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0004_auto_20210428_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]
