from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Bank(models.Model):
	CATEGORY_CHOICES = [
		('Займы', 'Займы'),
		('Кредиты', 'Кредиты'),
		('Кредитные карты', 'Кредитные карты'),
		('Дебитовые карты', 'Дебитовые карты'),
		('РКО', 'РКО'),
		('Залоги', 'Залоги'),
		('Автокредиты', 'Автокредиты'),
		('Ипотека', 'Ипотека'),
		('Рефинансирование', 'Рефинансирование'),
		('Для бизнеса', 'Для бизнеса')
	]

	FRAME_CHOICES = [
		('Нет', 'Нет'),
		('Зеленая', 'Зеленая'),
		('Красная', 'Красная'),
		('Синяя', 'Синяя'),
		('Светло-оранжевая', 'Светло-оранжевая'),
		('Ярко-красная', 'Ярко-красная'),
		('Сиреневая', 'Сиреневая'),
		('Светло-фиолетовый', 'Светло-фиолетовый'),
		('Салатовая', 'Салатовая'),
		('Светло-серая', 'Светло-серая'),
		('Бледно-голубая', 'Бледно-голубая'),
		('Голубая', 'Голубая'),
	]

	number_all = models.IntegerField(verbose_name='Номер приоритета в общем списке', default=0)
	number = models.IntegerField(verbose_name='Номер приоритета в списке категории', default=1)
	name = models.CharField(max_length=200, verbose_name='Название банка')
	country = models.CharField(max_length=200, verbose_name='Страна банка')
	offer_id = models.CharField(verbose_name='ID оффера в лидгиде', max_length=200)
	line1 = models.TextField(verbose_name='Строка 1')
	line2 = models.TextField(verbose_name='Строка 2')
	line3 = models.TextField(verbose_name='Строка 3')
	line4 = models.TextField(verbose_name='Строка 4', blank=True, null=True)
	description = models.TextField(verbose_name='Описание банка')
	photo = models.ImageField(upload_to='banks/', verbose_name='Логотип банка', blank=True, null=True)
	product_photo = models.ImageField(upload_to='products/', verbose_name='Фото продукта', blank=True, null=True)
	special_offer = models.CharField(max_length=200, verbose_name='Специальное предложение', null=True, blank=True)
	frame = models.CharField(max_length=200, verbose_name='Рамка', choices=FRAME_CHOICES, default='Нет')
	category = models.CharField(max_length=200, verbose_name='Вид кредитования', choices=CATEGORY_CHOICES, default='Займы')
	link = models.CharField(max_length=200, verbose_name='Ссылка на банк')
	is_active = models.BooleanField(default=True, verbose_name='Активен')

	class Meta:
		verbose_name = 'Банк'
		verbose_name_plural = 'Банки'

	def __str__(self):
		return self.name
