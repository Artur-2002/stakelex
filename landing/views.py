from django.shortcuts import render
from banks.models import Bank
import requests
from profiles.models import Profile
from django.contrib.gis.geoip2 import GeoIP2
from .models import *

# Create your views here.

def index(request, credit_type_param=None):
	credit_types1 = [
		'Кредиты',
		'Кредитные карты',
		'Дебитовые карты',
		'РКО',
		'Залоги',
		'Автокредиты',
		'Ипотека',
		'Рефинансирование',
		'Для бизнеса'
	]
	all_banks = Bank.objects.filter(is_active=True)

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	if ip != '127.0.0.1':
		g = GeoIP2()
		dictionary = {'Russia': '🇷🇺 RUS', 'Kazakhstan': '🇰🇿 KAZ', 'Ukraine': '🇺🇦 UKR'}
		
		try:
			all_banks = Bank.objects.filter(country=dictionary[g.country(ip)['country_name']])

		except:
			all_banks = Bank.objects.filter(country='🇷🇺 RUS')

		if request.user.is_authenticated:
			profile = Profile.objects.get(user=request.user)

			if profile.is_RU == True:
				all_banks = Bank.objects.filter(country='🇷🇺 RUS')

			if profile.is_UK == True:
				all_banks = Bank.objects.filter(country='🇺🇦 UKR')

			if profile.is_KAZ == True:
				all_banks = Bank.objects.filter(country='🇰🇿 KAZ')	

	credit_types = []

	for credit_type in credit_types1:
		for bank in all_banks:
			if bank.category == credit_type:
				credit_types.append(credit_type)
				break

	context = {
		'credit_type': credit_type_param,
		'credit_types': credit_types,
		'heading': Heading.objects.get(id=1),
		'extra_text': ExtraText.objects.get(id=1)
	}

	if credit_type_param == None:
		banks = []

		for bank in all_banks:
			if bank.category == 'Займы':
				banks.append(bank)

		banks.sort(key=lambda item: item.number)
		context['banks'] = banks

	else:
		banks = []

		for bank in all_banks:
			if bank.category == credit_type_param:
				banks.append(bank)

		banks.sort(key=lambda item: item.number)


		context['banks'] = banks

	return render(request, 'landing/index.html', context)




