# Generated by Django 2.1.5 on 2021-02-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_sponsor_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sponsor_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уникальный номер спонсора'),
        ),
    ]
