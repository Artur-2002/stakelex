from django.urls import path
from . import views


urlpatterns = [
	path('', views.index),
	path('<credit_type_param>/', views.index),
]