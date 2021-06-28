# Generated by Django 2.1.5 on 2021-05-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0012_bank_frame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='frame',
            field=models.CharField(choices=[(0, 'Нет'), (1, 'Зеленая'), (2, 'Красная'), (3, 'Синяя')], default='Нет', max_length=200, verbose_name='Рамка'),
        ),
    ]
