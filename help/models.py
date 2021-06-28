from django.db import models
from profiles.models import Profile

# Create your models here.

class ProfileRequest(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль пользователя')
	name = models.CharField(max_length=200, verbose_name='Имя')
	email = models.CharField(max_length=200, verbose_name='Email')
	subject = models.CharField(max_length=200, verbose_name='Тема')
	message = models.TextField(verbose_name='Сообщение')
	completed = models.BooleanField(verbose_name='Завершено', default=False)

	class Meta:
		verbose_name = 'Сообщение пользователя'
		verbose_name_plural = 'Сообщения пользователей'

	def __str__(self):
		return self.subject


	def save(self, *args, **kwargs):
		self.email = self.profile.email

		super(ProfileRequest, self).save(*args, **kwargs)