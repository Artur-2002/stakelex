from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.

def delete_profile(modeladmin, request, queryset):
	for obj in queryset:
		if obj.sponsor_number != None:
			sponsor = Profile.objects.get(number=obj.sponsor_number)
			sponsor.referal1_count -= 1

			for i in range(len(sponsor.referals1_numbers)):
				if sponsor.referals1_numbers[i] == obj.number:
					del sponsor.referals1_numbers[i]
					break

			sponsor.save()

			if sponsor.sponsor_number != None:
				sponsor2 = Profile.objects.get(number=sponsor.sponsor_number)
				sponsor2.referal2_count -= 1

				for i in range(len(sponsor2.referals2_numbers)):
					if sponsor2.referals2_numbers[i] == obj.number:
						del sponsor2.referals2_numbers[i]
						break

				sponsor2.save()

				if sponsor2.sponsor_number != None:
					sponsor3 = Profile.objects.get(number=sponsor2.sponsor_number)
					sponsor3.referal3_count -= 1

					for i in range(len(sponsor3.referals3_numbers)):
						if sponsor3.referals3_numbers[i] == obj.number:
							del sponsor3.referals3_numbers[i]
							break

					sponsor3.save()

					if sponsor3.sponsor_number != None:
						sponsor4 = Profile.objects.get(number=sponsor3.sponsor_number)
						sponsor4.referal4_count -= 1

						for i in range(len(sponsor4.referals4_numbers)):
							if sponsor4.referals4_numbers[i] == obj.number:
								del sponsor4.referals4_numbers[i]
								break

						sponsor4.save()

		obj.delete()

delete_profile.short_description = "Удалить выбранные Профили"

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['ava', 'number', 'email', 'admin_login']
	search_fields = ('number', 'email')
	list_filter = ['country']
	actions = [delete_profile]

	def ava(self, obj):
		url = obj.avatar.url
		return format_html(f"<img src='{url}' style='width: 35px; height: 35px;'>", url=url)

	ava.short_description = 'Аватар'

	def admin_login(self, obj):
		if obj.user.is_superuser == False:
			url = f'/admin_login/{obj.email}'
			return format_html(f"<a href='{url}'>Войти в кабинет</a>", url=url)
		else:
			return format_html(f"<p>Нет доступных действий</p>")
	admin_login.short_description = 'Действия'

	def get_actions(self, request):
		actions = super(ProfileAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']

		return actions

admin.site.register(Profile, ProfileAdmin)