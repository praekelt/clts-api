from django.contrib import admin

from .models import CommunityChampion, Activation


class CommunityChampionAdmin(admin.ModelAdmin):
	list_display = ('name', 'msisdn',)


class ActivationAdmin(admin.ModelAdmin):
	list_filter = ('activation_date',)
	list_display = ('entered', 'matched', 'activation_date',)
	readonly_fields = ('activation_date',)


admin.site.register(CommunityChampion, CommunityChampionAdmin)
admin.site.register(Activation, ActivationAdmin)
