from django.contrib import admin

from .models import Champion


class ChampionAdmin(admin.ModelAdmin):
	list_filter = ('activated', 'activation_date',)
	list_display = ('name', 'msisdn', 'activated')

admin.site.register(Champion, ChampionAdmin)
