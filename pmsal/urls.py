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
    # url(r'^representantes/', 'canaa.core.views.sellers', name='sellers'),
    # url(r'^marketing/', 'canaa.core.views.marketing', name='marketing'),
    url(r'^contato/', 'pmsal.core.views.contact', name='contact'),

    # url(r'^trabalhe-conosco/', include('canaa.talents.urls')),
    url(r'^agenda/', include('pmsal.event.urls', namespace='event')),
    url(r'^noticias/', include('pmsal.blog.urls', namespace='blog')),
    # url(r'^produtos/', include('canaa.catalog.urls', namespace='group')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# )
