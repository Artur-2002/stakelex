# Generated by Django 2.1.5 on 2021-02-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_codeforemail_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referal_link',
            field=models.CharField(default='None', max_length=200, verbose_name='Реферальная ссылка'),
        ),
    ]
