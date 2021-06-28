from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.

class BankAdmin(admin.ModelAdmin):
	list_display = ['logo', 'name', 'offer_id', 'number', 'number_all', 'country']
	list_filter = ['country', 'category']
	search_fields = ('name', 'description')

	def logo(self, obj):
		if obj.photo:
			url = obj.photo.url
			return format_html(f"<img src='{url}' style='width: 35px; height: 35px;'>", url=url)

		return format_html("<div style='width: 35px; height: 35px; background-color: grey'></div>")

	logo.short_description = 'Логотип'

admin.site.register(Bank, BankAdmin)