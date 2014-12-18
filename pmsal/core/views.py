# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template import RequestContext

from pmsal.context_processors import enterprise_proc

from pmsal.core.models import (Link, Program, Banner, Category, Content,
                               Timeline)
from pmsal.event.models import Calendar
from pmsal.blog.models import Entry

from pmsal.core.forms import ContactForm


def home(request):
    context = {}
    context['link_list'] = Link.objects.all()
    context['program_list'] = Program.objects.all()
    context['calendar_list'] = Calendar.objects.all()
    context['blog_list'] = Entry.published.all()[:4]
    context['super_banner_list'] = Banner.published.filter(type=1)
    context['second_banner_list'] = Banner.published.filter(type=2)
    context['popup_banner_list'] = Banner.published.filter(type=3)[:1]

    return render(request, 'home.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def contact(request):
    context = {}

    # contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            context['contact_success'] = True
    else:
        form = ContactForm()

    context['contact_form'] = form

    return render(request, 'contact.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def content(request, slug):
    context = {}

    category = Category.objects.filter(slug=slug)

    content_list = get_object_or_404(Content, category=category)
    # try:
    # except:
    #     content_list = ''

    context['content_list'] = content_list
    context['blog_list'] = Entry.published.filter(categories=category)[:4]

    return render(request, 'content.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def city(request):
    context = {}

    context['timeline_list'] = Timeline.objects.all()

    return render(request, 'institutional.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def transparency(request):
    context = {}

    pagina = request.GET.get('pagina', '')
    if pagina:
        context['pagina'] = pagina

    return render(request, 'transparenciasaloa.html', context)
    # return redirect('http://saloa.pe.gov.br/transparencia/')
