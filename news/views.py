# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from main.models import MainSlider
from news.models import News


class NewsListView(ListView):
    model = News
    context_object_name = "news_ad"
    paginate_by = 5
    template_name = 'news_list.html'

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['slider'] = MainSlider.objects.all()
        print context['news_ad']
        return context
