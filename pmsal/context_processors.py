# coding: utf-8
from django.shortcuts import get_object_or_404

from pmsal.core.models import Enterprise


def enterprise_proc(request):
    """ View Function """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    return {
        'enterprise': enterprise,
    }


class EnterpriseExtraContext(object):
    """ Class Based View """
    extra_context = {}
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''
    extra_context = {'enterprise': enterprise}

    def get_context_data(self, **kwargs):
        context = super(EnterpriseExtraContext,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
