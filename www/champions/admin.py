from django.contrib import admin

from .models import Champion, Village


class ChampionAdmin(admin.ModelAdmin):
    list_filter = ('activated', 'activation_date',)
    list_display = ('name', 'msisdn', 'activated')


class VillageAdmin(admin.ModelAdmin):
    list_filter = ('champion',)
    list_display = ('name', 'champion')

admin.site.register(Champion, ChampionAdmin)
admin.site.register(Village, VillageAdmin)
