# coding: utf-8
from django import forms

from pmsal.bid.models import Entry


class EntryForm(forms.ModelForm):
    description = forms.CharField(
        label='Objeto da Licitação',
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 6}))

    class Meta:
        model = Entry
