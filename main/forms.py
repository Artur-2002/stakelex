from django import forms


class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Пароль'}))


class RegisterForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}))
	agree = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'id': 'agreeTerms', 'name': 'terms', 'value': 'agree'}))


class ResetForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}))


class ProfileRequestForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'inputName', 'class': 'form-control'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'inputSubject', 'class': 'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'id': 'inputMessage', 'class': 'form-control', 'rows': '4'}))
