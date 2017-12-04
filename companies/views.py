# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from companies.models import Companies
from main.models import MainSlider


class CompaniesListView(ListView):
    model = Companies
    context_object_name = 'companies_ad'
    template_name = 'companies.html'

    def get_context_data(self, **kwargs):
        context = super(CompaniesListView,self).get_context_data(**kwargs)
        context['slider'] = MainSlider.objects.all()
        return context