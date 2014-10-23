# coding: utf-8
from django.db.models import Q
from django.views import generic

from pmsal.context_processors import EnterpriseExtraContext

from pmsal.bid.models import Entry


class EntryListView(EnterpriseExtraContext,  generic.ListView):
    model = Entry
    template_name = 'bid/entry_home.html'
    # TODO: mudar a paginacao
    paginate_by = 20

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        if search:
            obj_lst = Entry.objects.filter(Q(description__icontains=search))
        else:
            obj_lst = Entry.objects.all()
        return obj_lst

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search', '')
        context['search'] = search
        return context
