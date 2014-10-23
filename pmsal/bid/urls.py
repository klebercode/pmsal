# coding: utf-8
from django.conf.urls import patterns, url

from pmsal.bid.views import EntryListView


urlpatterns = patterns(
    'pmsal.bid.views',
    url(r'^$', EntryListView.as_view(), name='home'),
)
