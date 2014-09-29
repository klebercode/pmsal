# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from tinymce import models as tinymce_models
from taggit.managers import TaggableManager

from pmsal.current_user import get_current_user
from pmsal.core.models import Category


class EntryManager(models.Manager):
    '''
    Esse manager carrega todos os objetos do model Entry sem filtros
    '''
    def get_queryset(self):
        return super(EntryManager,
                     self).get_queryset().all()


class PublishedManager(models.Manager):
    '''
    Esse manager carrega todos os objetos do model Entry que estao marcados
    como publish=True
    '''
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(publish=True)


class Entry(models.Model):
    title = models.CharField(_(u'Título da Notícia'), max_length=200)
    slug = models.SlugField(_(u'Link no Site'), max_length=200,
                            unique=True)
    image = models.ImageField(_(u'Imagem da Notícia'), upload_to='blog')
    body = tinymce_models.HTMLField(_(u'Texto'))
    publish = models.BooleanField(_(u'Publicar no site?'), default=True)
    created = models.DateTimeField(_(u'Data de Criação'), auto_now_add=True)
    modified = models.DateTimeField(_(u'Data de Modificação'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_(u'Autor'),
                               editable=False, default=get_current_user)
    categories = models.ManyToManyField(Category,
                                        verbose_name=_(u'Categorias'))

    tags = TaggableManager()
    # quando precisar chamar todos os objetos sem filtro:
    # Entry.objects.all()
    objects = EntryManager()
    # quando precisar chamar apenas os objetos com publish=True:
    # Entry.published.all()
    published = PublishedManager()

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem da Notícia'

    def save(self, *args, **kwargs):
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:entry_date_detail',
                       kwargs={'year': self.created.year,
                               'month': self.created.strftime('%m'),
                               'day': self.created.strftime('%d'),
                               'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Notícia')
        verbose_name_plural = _(u'Notícias')
        ordering = ['-created', 'title', 'author']
