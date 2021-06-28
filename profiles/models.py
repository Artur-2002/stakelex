from django.db import models
import random
import string
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import datetime

# Create your models here.

class ProfileQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in self:
            obj.user.delete()
        super(ProfileQuerySet, self).delete(*args, **kwargs)

class Profile(models.Model):
	LANGUAGE_CHOICES = [
		('ru', 'ru'),
		('en', 'en'),
		('es', 'es'),
	]
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар пользователя', default='/avatars/avatar_default.png')
	number = models.CharField(max_length=200, verbose_name='Уникальный номер', default="0", unique=True)
	email = models.EmailField(verbose_name='Email пользователя', unique=True)
	referal_link = models.CharField(max_length=200, verbose_name='Реферальная ссылка', default='None', unique=True)
	sponsor_number = models.CharField(max_length=200, verbose_name='Уникальный номер спонсора', null=True, blank=True)
	referal1_count = models.IntegerField(verbose_name='Кол-во рефералов в первой линии', default=0)
	referals1_numbers = ArrayField(models.CharField(max_length=200), null=True, blank=True, default=[], verbose_name='Номера рефералов в 1 линии')
	referal2_count = models.IntegerField(verbose_name='Кол-во рефералов во второй линии', default=0)
	referals2_numbers = ArrayField(models.CharField(max_length=200), null=True, blank=True, default=[], verbose_name='Номера рефералов в 2 линии')
	referal3_count = models.IntegerField(verbose_name='Кол-во рефералов в третьей линии', default=0)
	referals3_numbers = ArrayField(models.CharField(max_length=200), null=True, blank=True, default=[], verbose_name='Номера рефералов в 3 линии')
	referal4_count = models.IntegerField(verbose_name='Кол-во рефералов в четвертой линии', default=0)
	referals4_numbers = ArrayField(models.CharField(max_length=200), null=True, blank=True, default=[], verbose_name='Номера рефералов в 4 линии')
	language = models.CharField(max_length=200, verbose_name='Язык пользователя', default='ru', choices=LANGUAGE_CHOICES)
	country = models.CharField(max_length=200, verbose_name='Страна пользователя', default='None')
	country_code = models.CharField(max_length=200, verbose_name='Код страны', default='None')
	ip = models.CharField(max_length=200, verbose_name='IP пользователя', default='None')
	register_date = models.DateTimeField(verbose_name='Дата и время регистрации', default=datetime.now())
	is_RU = models.BooleanField(default=False, verbose_name='Отображать только Российские банки')
	is_UK = models.BooleanField(default=False, verbose_name='Отображать только Украинские банки')
	is_KAZ = models.BooleanField(default=False, verbose_name='Отображать только Казахстанские банки')

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

	def __str__(self):
		return self.email

	def save(self, *args, **kwargs):
		if self.number == None or self.number == "0":
			self.number = ''.join(random.choice(string.digits) for i in range(10))

		if self.referal_link == None or self.referal_link == "None":
			self.referal_link = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(10))

		super(Profile, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		self.user.delete()
		super(Profile, self).delete(*args, **kwargs)


class CodeForEmail(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	code = models.CharField(max_length=200)
	email = models.EmailField()


class Country(models.Model):
	logo = models.CharField(max_length=200)
	name = models.CharField(max_length=200)