from django.contrib import admin
from .models import *

# Register your models here.

class ProfileRequestAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'subject', 'completed']
	list_filter = ['completed']
	search_fields = ('name', 'email', 'subject', 'message')

admin.site.register(ProfileRequest, ProfileRequestAdmin)