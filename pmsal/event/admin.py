# coding: utf-8
from django.contrib import admin

from pmsal.event.models import Calendar


class CalendarAdmin(admin.ModelAdmin):
    list_filter = ('date_start', 'date_end', 'created_by__username')
    list_display = ('title', 'date_start', 'date_end')
    search_fields = ('title', 'date_start', 'date_end', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_start'


admin.site.register(Calendar, CalendarAdmin)
