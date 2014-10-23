# coding: utf-8
from django.contrib import admin

from mce_filebrowser.admin import MCEFilebrowserAdmin

from pmsal.core.models import (Enterprise, Social, Category, Link, Program,
                               Banner, Content, Timeline)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'phone3', 'email')
    search_fields = ('name', 'description', 'address', 'number', 'complement',
                     'cep', 'district', 'city', 'state',
                     'phone1', 'phone2', 'phone3', 'email')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('area',)
    list_display = ('name', 'acronym', 'area')
    search_fields = ('name', 'acronym', 'area')
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


class ContentAdmin(MCEFilebrowserAdmin):
    list_filter = ('category',)
    list_display = ('category', 'admin_body')
    search_fields = ('body',)


class TimelineAdmin(admin.ModelAdmin):
    list_filter = ('period',)
    list_display = ('title', 'period', 'admin_image', 'description')
    search_fields = ('title', 'period', 'description')


admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Social)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Timeline, TimelineAdmin)
