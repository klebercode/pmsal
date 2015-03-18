from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'pmsal.core.views.home', name='home'),
    # url(r'^institucional/', 'canaa.core.views.institutional',
    #     name='institutional'),

    url(r'^a-prefeitura/', 'pmsal.core.views.city', name='city'),
    url(r'^contato/', 'pmsal.core.views.contact', name='contact'),
    url(r'^transparencia/', 'pmsal.core.views.transparency',
        name='transparency'),

    url(r'^prefeitura/(?P<slug>[-\w]+)/$', 'pmsal.core.views.content',
        name='prefeitura'),
    url(r'^imprensa/(?P<slug>[-\w]+)/$', 'pmsal.core.views.content',
        name='imprensa'),
    url(r'^secretaria/(?P<slug>[-\w]+)/$', 'pmsal.core.views.content',
        name='secretaria'),

    url(r'^agenda/', include('pmsal.event.urls', namespace='event')),
    url(r'^noticias/', include('pmsal.blog.urls', namespace='blog')),
    url(r'^licitacoes/', include('pmsal.bid.urls', namespace='bid')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# )
