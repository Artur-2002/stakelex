# Generated by Django 2.1.5 on 2021-02-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_codeforemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeforemail',
            name='email',
            field=models.EmailField(default='test@email.ru', max_length=254),
            preserve_default=False,
        ),
    ]
