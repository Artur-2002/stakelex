# Generated by Django 2.1.5 on 2021-05-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Дополнительный текст',
                'verbose_name_plural': 'Дополнительный текст',
            },
        ),
    ]