# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

import uuid
import os


class Entry(models.Model):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('licitacao', filename)

    created = models.DateTimeField(_(u'Data de Criação'), auto_now_add=True)
    modified = models.DateTimeField(_(u'Data de Modificação'), auto_now=True)
    description = models.TextField(_(u'Objeto da Licitação'))
    process = models.CharField(_(u'Processo Licitatório Nº'), max_length=20)
    price = models.CharField(_(u'Tomada de Preços Nº'), max_length=20)
    attach = models.FileField(_(u'Arquivo'), upload_to=get_file_path,
                              help_text='Selecione um arquivo')

    def admin_attach(self):
        if self.attach:
            return "<a href='%s'>Baixar</a>" % self.attach.url
        else:
            return "Nenhum arquivo encontrado"
    admin_attach.allow_tags = True
    admin_attach.short_description = _(u'Arquivo')

    def __unicode__(self):
        return unicode(self.process)

    class Meta:
        verbose_name = _(u'Licitação')
        verbose_name_plural = _(u'Licitações')
        ordering = ['-created', 'description', 'process', 'price']
