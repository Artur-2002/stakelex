from django.db import models

# Create your models here.


class Heading(models.Model):
	text = models.TextField(verbose_name='Текст заголовка')

	class Meta:
		verbose_name = 'Заголовок'
		verbose_name_plural = 'Заголовок'


class ExtraText(models.Model):
	text = models.TextField(verbose_name='Текст')

	class Meta:
		verbose_name = 'Дополнительный текст'
		verbose_name_plural = 'Дополнительный текст'