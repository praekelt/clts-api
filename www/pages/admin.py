from django.contrib import admin

from .models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    slug_fields = {'slug': 'name'}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
