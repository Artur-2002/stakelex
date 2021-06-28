from django.shortcuts import render
from profiles.models import Profile, CodeForEmail, Country
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, ResetForm, ProfileRequestForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import string
import random
from django import forms
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from django.contrib.gis.geoip2 import GeoIP2
from help.models import ProfileRequest
from banks.models import Bank
import requests

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		profile.ip = ip
		profile.save()

		g = GeoIP2()

		if ip != '127.0.0.1':
			try:
				c = Country.objects.get(name=g.country(ip)['country_name'])
				profile.country = g.country(ip)['country_name']
				profile.country_code = c.logo + ' ' + g.country(ip)['country_code']
				profile.save()

			except:
				pass

		return render(request, 'main/index.html', {'profile': profile})

	else:
		return HttpResponseRedirect('/start/')


def user_login(request):
	error = ''
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			try:
				user = authenticate(username=cd['email'], password=cd['password'])
				login(request, user)
				return HttpResponseRedirect('/')

			except:
				error = 'Неверный логин или пароль'
	
	else:
		form = LoginForm()
	return render(request, 'main/login.html', {'form': form,'error': error})


def user_register(request, link=None):
	error = ''
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			try:
				user = User.objects.get(username=cd['email'])
				error = 'Эта почта уже используется'

			except:
				password = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(10))
				user = User(username=cd['email'])
				user.save()
				user.set_password(password)
				user.save()

				if link != None:
					try:
						sponsor = Profile.objects.get(referal_link=link)
						profile = Profile.objects.create(user=user, email=cd['email'])
						profile.save()
						profile.sponsor_number = sponsor.number
						sponsor.referal1_count += 1
						sponsor.referals1_numbers.append(profile.number)
						profile.save()
						sponsor.save()

						if sponsor.sponsor_number != None:
							sponsor2 = Profile.objects.get(number=sponsor.sponsor_number)
							sponsor2.referal2_count += 1
							sponsor2.referals2_numbers.append(profile.number)
							sponsor2.save()

							if sponsor2.sponsor_number != None:
								sponsor3 = Profile.objects.get(number=sponsor2.sponsor_number)
								sponsor3.referal3_count += 1
								sponso3.referals3_numbers.append(profile.number)
								sponsor3.save()

								if sponsor3.sponsor_number != None:
									sponsor4 = Profile.objects.get(number=sponsor3.sponsor_number)
									sponsor4.referal4_count += 1
									sponsor4.referals4_numbers.append(profile.number)
									sponsor4.save()

					except:
						profile = Profile.objects.create(user=user, email=cd['email'])
						profile.save()

				else:
					profile = Profile.objects.create(user=user, email=cd['email'])
					profile.save()

				fromaddr = "*****"
				toaddr = cd['email']
				mypass = '*****'
				msg = MIMEMultipart()
				msg['From'] = formataddr((str(Header('STAKELEX', 'utf-8')), fromaddr))
				msg['To'] = toaddr
				msg['Subject'] = "Временный пароль для входа"
					 
				body = f"Ваш временный паролль: {password}"
				msg.attach(MIMEText(body, 'plain'))
					 
				server = smtplib.SMTP('smtp.mail.ru', 587)
				server.starttls()
				server.login(fromaddr, mypass)
				text = msg.as_string()
				server.sendmail(fromaddr, toaddr, text)
				server.quit()

				return HttpResponseRedirect('/successful/')
	
	else:
		form = RegisterForm()
	return render(request, 'main/register.html', {'form': form,'error': error})


def successful(request):
	return render(request, 'main/successful.html')


def reset_password(request):
	error = ''
	if request.method == 'POST':
		form = ResetForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			try:
				user = User.objects.get(username=cd['email'])
				password = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(10))
				user.set_password(password)
				user.save()

				fromaddr = "****"
				toaddr = cd['email']
				mypass = '****'
				msg = MIMEMultipart()
				msg['From'] = formataddr((str(Header('STAKELEX', 'utf-8')), fromaddr))
				msg['To'] = toaddr
				msg['Subject'] = "Временный пароль для входа"
					 
				body = f"Ваш временный пароль: {password}"
				msg.attach(MIMEText(body, 'plain'))
					 
				server = smtplib.SMTP('smtp.mail.ru', 587)
				server.starttls()
				server.login(fromaddr, mypass)
				text = msg.as_string()
				server.sendmail(fromaddr, toaddr, text)
				server.quit()

				return HttpResponseRedirect('/successful/')

			except:
				error = 'Аккаунта с такой почтой не существует'
				form = ResetForm()
				return render(request, 'main/reset_password.html', {'form': form, 'error': error})
	
	else:
		form = ResetForm()
	return render(request, 'main/reset_password.html', {'form': form,'error': error})


def profile(request):
	error1 = ''
	error2 = ''

	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')


	class ChangeEmailForm(forms.Form):
		email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Новый email'}))

	class ChangePasswordForm(forms.Form):
		password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Текущий пароль'}))
		new_password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Новый пароль'}))
		new_password_agree = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Подтверждение новго пароля'}))

	form1 = ChangeEmailForm()
	form2 = ChangePasswordForm()
	if request.method == 'POST':
		if 'change_email' in request.POST:
			form1 = ChangeEmailForm(request.POST)

			if form1.is_valid():
				cd = form1.cleaned_data
				try:
					profile_check = Profile.objects.get(email=cd['email'])
					error1 = 'Эта почта уже используется'
					form1 = ChangeEmailForm()
					form2 = ChangePasswordForm()

					return render(request, 'main/profile.html', {'profile': profile, 'form1': form1, 'form2': form2, 'error1': error1, 'error2': error2})

				except:
					code = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(5))
					fromaddr = "****"
					toaddr = cd['email']
					mypass = '****'
					msg = MIMEMultipart()
					msg['From'] = formataddr((str(Header('STAKELEX', 'utf-8')), fromaddr))
					msg['To'] = toaddr
					msg['Subject'] = "Код подтверждения"
							 
					body = f"Ваш код подтверждения для смены почты: {code}"
					msg.attach(MIMEText(body, 'plain'))
							 
					server = smtplib.SMTP('smtp.mail.ru', 587)
					server.starttls()
					server.login(fromaddr, mypass)
					text = msg.as_string()
					server.sendmail(fromaddr, toaddr, text)
					server.quit()

					for ce in CodeForEmail.objects.filter(profile=profile):
						ce.delete()

					c = CodeForEmail.objects.create(profile=profile, code=code, email=cd['email'])

					return HttpResponseRedirect('/change_email/')


		elif 'change_password' in request.POST:
			form2 = ChangePasswordForm(request.POST)

			if form2.is_valid():
				cd = form2.cleaned_data

				if request.user.check_password(cd['password']):
					if cd['new_password'] == cd['new_password_agree']:
						request.user.set_password(cd['new_password'])
						request.user.save()
						logout(request)

						return HttpResponseRedirect('/login/')

					else:
						error2 = 'Пароли не совпадают'
						form1 = ChangeEmailForm()
						form2 = ChangePasswordForm()
						return render(request, 'main/profile.html', {'profile': profile, 'form1': form1, 'form2': form2, 'error1': error1, 'error2': error2})

				else:
					error2 = 'Неверный пароль'
					form1 = ChangeEmailForm()
					form2 = ChangePasswordForm()
					return render(request, 'main/profile.html', {'profile': profile, 'form1': form1, 'form2': form2, 'error1': error1, 'error2': error2})

	else:
		form1 = ChangeEmailForm()
		form2 = ChangePasswordForm()

	return render(request, 'main/profile.html', {'profile': profile, 'form1': form1, 'form2': form2, 'error1': error1, 'error2': error2})



def change_email(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)
	else:
		return HttpResponseRedirect('/login/')

	class CodeForm(forms.Form):
		code = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Введите код подтверждения'}))

	if request.method == 'POST':
		code = CodeForEmail.objects.get(profile=profile)
		form = CodeForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data

			if code.code == cd['code']:
				profile.email = code.email
				profile.save()
				request.user.username = code.email
				request.user.save()
				code.delete()

				logout(request)

				return HttpResponseRedirect('/login/')

			else:
				return render(request, 'main/code_error.html')


	else:
		form = CodeForm()

	return render(request, 'main/change_email.html', {'profile': profile, 'form': form})


def change_language_ru(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	profile.language = 'ru'
	profile.save()

	return HttpResponseRedirect("/")

def change_language_en(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	profile.language = 'en'
	profile.save()

	return HttpResponseRedirect("/")

def change_language_es(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	profile.language = 'es'
	profile.save()

	return HttpResponseRedirect("/")



def user_logout(request):
	if request.user.is_authenticated:
		logout(request)


	return HttpResponseRedirect('/login/')


def structure(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	registers = len(Profile.objects.all())
	group = []
	countries = []
	line1 = []

	for number in profile.referals1_numbers:
		group.append(Profile.objects.get(number=number))
		line1.append(Profile.objects.get(number=number))

	for number in profile.referals2_numbers:
		group.append(Profile.objects.get(number=number))

	for number in profile.referals3_numbers:
		group.append(Profile.objects.get(number=number))

	for number in profile.referals4_numbers:
		group.append(Profile.objects.get(number=number))

	for referal in group:
		if referal.country_code not in countries:
			countries.append(referal.country_code)

	context = {
		'profile': profile,
		'registers': registers,
		'countries': len(countries),
		'first_level': profile.referal1_count,
		'group': len(group),
		'line1': line1,
	}

	return render(request, 'main/structure.html', context)


def help(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	if request.method == 'POST':
		form = ProfileRequestForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data

			profile_request = ProfileRequest.objects.create(profile=profile, name=cd['name'], subject=cd['subject'], message=cd['message'])

			return HttpResponseRedirect('/help/')

	else:
		form = ProfileRequestForm()

	return render(request, 'main/help.html', {'profile': profile, 'form': form})


def credit(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	countries = []
	banks = Bank.objects.all()
	credit_types = []

	for bank in banks:
		if bank.country not in countries:
			countries.append(bank.country)

		for credit_type in bank.categories:
			if credit_type not in credit_types:
				credit_types.append(credit_type)


	context = {
		'profile': profile,
		'countries': sorted(countries),
		'credit_types': sorted(credit_types),
	}

	return render(request, 'main/credit.html', context)


def banks(request, country, category):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	if country == 'all':
		banks = Bank.objects.all()

	else:
		banks = Bank.objects.filter(country=country)

	if category != 'all':
		new_banks = []

		for bank in banks:
			if category in bank.categories:
				new_banks.append(bank)

		banks = new_banks

	return render(request, 'main/banks.html', {'profile': profile, 'banks': banks})


def bank(request, name):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	bank = Bank.objects.get(name=name)

	return render(request, 'main/bank.html', {'profile': profile, 'bank': bank})


def bonus(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	return render(request, 'main/bonus.html', {'profile': profile})


def admin_login(request, username):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

	else:
		return HttpResponseRedirect('/login/')

	if request.user.is_superuser:
		user = User.objects.get(username=username)
		login(request, user)

	return HttpResponseRedirect('/')




