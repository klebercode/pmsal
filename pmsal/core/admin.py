# coding: utf-8
from django.contrib import admin

from pmsal.core.models import (Enterprise, Social, Category, Link, Program,
                               Banner)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'phone3', 'email')
    search_fields = ('name', 'description', 'address', 'number', 'complement',
                     'cep', 'district', 'city', 'state',
                     'phone1', 'phone2', 'phone3', 'email')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')
    search_fields = ('name', 'acronym')
    prepopulated_fields = {'slug': ('name',)}


class LinkAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'name', 'link')
    search_fields = ('name',)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'name', 'link')
    search_fields = ('name',)


class BannerAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('admin_image', 'title', 'type', 'publish')
    search_fields = ('title',)


admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Social)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Banner, BannerAdmin)
