# Generated by Django 2.1.5 on 2021-05-31 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0015_auto_20210506_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='special_offer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Специальное предложение'),
        ),
    ]
