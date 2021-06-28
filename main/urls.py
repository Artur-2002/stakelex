from django.urls import path
from . import views


urlpatterns = [
	path('', views.index),
	path('login/', views.user_login),
	path('register/<link>/', views.user_register),
	path('register/', views.user_register),
	path('successful/', views.successful),
	path('reset_password/', views.reset_password),
	path('profile/', views.profile),
	path('change_email/', views.change_email),
	path('ru/', views.change_language_ru),
	path('en/', views.change_language_en),
	path('es/', views.change_language_es),
	path('logout/', views.user_logout),
	path('structure/', views.structure),
	path('help/', views.help),
	path('credit/', views.credit),
	path('credit/<country>/<category>/', views.banks),
	path('bank/<name>/', views.bank),
	path('bonus/', views.bonus),
	path('admin_login/<username>/', views.admin_login),
]