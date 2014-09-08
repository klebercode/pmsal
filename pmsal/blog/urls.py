# coding: utf-8
from django.conf.urls import patterns, url

from pmsal.blog.views import (EntryYearArchiveView, EntryMonthArchiveView,
                              EntryDayArchiveView, EntryListView,
                              EntryDateDetailView, EntryTagListView,
                              EntryCategoryListView)


urlpatterns = patterns(
    'pmsal.blog.views',
    url(r'^$', EntryListView.as_view(), name='home'),
    url(r'^(?P<year>\d{4})/$',
        EntryYearArchiveView.as_view(),
        name='entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$',
        EntryMonthArchiveView.as_view(month_format='%m'),
        name='entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
        EntryDayArchiveView.as_view(month_format='%m'),
        name='entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$',
        EntryDateDetailView.as_view(month_format='%m'),
        name='entry_date_detail'),
    url(r'^marcacao/(?P<tag_slug>[-\w]+)/$', EntryTagListView.as_view(),
        name='tag_list'),
    url(r'^categoria/(?P<cat_slug>[-\w]+)/$', EntryCategoryListView.as_view(),
        name='category_list'),
)

# chama a pagina sem precisar criar a view
# apenas passando os parametros na url
    # url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$',
    #     DateDetailView.as_view(month_format='%m', model=Entry,
    #                            date_field='created',
    #                            allow_future=True),
    #     name='entry_date_detail'),
