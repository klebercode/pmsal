# coding: utf-8
from django.shortcuts import get_object_or_404

from pmsal.core.models import Enterprise, Category, AREA_CHOICES


def enterprise_proc(request):
    """ View Function """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    area_reverse = dict((v, k) for k, v in AREA_CHOICES)
    prefeitura = Category.objects.filter(area=area_reverse['Prefeitura'])
    imprensa = Category.objects.filter(area=area_reverse['Imprensa'])
    secretarias = Category.objects.filter(area=area_reverse['Secretarias'])

    return {
        'enterprise': enterprise,
        'prefeitura': prefeitura,
        'imprensa': imprensa,
        'secretarias': secretarias,
    }


class EnterpriseExtraContext(object):
    """ Class Based View """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    area_reverse = dict((v, k) for k, v in AREA_CHOICES)
    prefeitura = Category.objects.filter(area=area_reverse['Prefeitura'])
    imprensa = Category.objects.filter(area=area_reverse['Imprensa'])
    secretarias = Category.objects.filter(area=area_reverse['Secretarias'])

    extra_context = {
        'enterprise': enterprise,
        'prefeitura': prefeitura,
        'imprensa': imprensa,
        'secretarias': secretarias,
        }

    def get_context_data(self, **kwargs):
        context = super(EnterpriseExtraContext,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
