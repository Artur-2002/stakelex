# Generated by Django 2.1.5 on 2021-05-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0014_auto_20210503_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='category',
            field=models.CharField(choices=[('Займы', 'Займы'), ('Кредиты', 'Кредиты'), ('Кредитные карты', 'Кредитные карты'), ('Дебитовые карты', 'Дебитовые карты'), ('РКО', 'РКО'), ('Залоги', 'Залоги'), ('Автокредиты', 'Автокредиты'), ('Ипотека', 'Ипотека'), ('Рефинансирование', 'Рефинансирование'), ('Для бизнеса', 'Для бизнеса')], default='Займы', max_length=200, verbose_name='Вид кредитования'),
        ),
    ]