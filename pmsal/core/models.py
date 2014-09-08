# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


STATE_CHOICES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)


class Social(models.Model):
    name = models.CharField(_(u'Nome'), max_length=50,
                            help_text='Ex: Facebook')
    link = models.URLField(_(u'Link'),
                           help_text='Ex: http://www.facebook.com/usuario')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Mídia Social')
        verbose_name_plural = _(u'Mídias Sociais')
        ordering = ['name']


class Enterprise(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    description = models.CharField(_(u'Descrição'), max_length=100,
                                   blank=True, null=True)
    cnpj = models.CharField(_(u'CNPJ'), max_length=20,
                            help_text='99.999.999/9999-99')
    address = models.CharField(_(u'Endereço'), max_length=200)
    number = models.CharField(_(u'Número'), max_length=10)
    complement = models.CharField(_(u'Complemento'), max_length=100,
                                  blank=True, null=True)
    cep = models.CharField(_(u'CEP'), max_length=9, help_text='99999-999',
                           blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100)
    city = models.CharField(_(u'Cidade'), max_length=100)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    country = models.CharField(_(u'País'), max_length=50)
    phone1 = models.CharField(_(u'Fone 1'), max_length=20,
                              help_text='(99) 9999-9999')
    phone2 = models.CharField(_(u'Fone 2'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    phone3 = models.CharField(_(u'Fone 3 (Fax)'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    email = models.EmailField(_(u'Email'))
    site = models.URLField(_(u'Site'))
    socials = models.ManyToManyField('Social',
                                     verbose_name=_(u'Mídias Sociais'))

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Empresa')
        verbose_name_plural = _(u'Empresa')


class Category(models.Model):
    name = models.CharField(_(u'Nome'), max_length=200)
    slug = models.SlugField(_(u'Link no site'), max_length=200,
                            unique=True)
    acronym = models.CharField(_(u'Sigla'), max_length=50, blank=True,
                               null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category_list', kwargs={'pk': self.pk})

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')
        ordering = ['name']
