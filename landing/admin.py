from django.contrib import admin
from .models import *

# Register your models here.


class HeadingAdmin(admin.ModelAdmin):
	list_display = ['text']

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(Heading, HeadingAdmin)


class ExtraTextAdmin(admin.ModelAdmin):
	list_display = ['text']
	
	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(ExtraText, ExtraTextAdmin)