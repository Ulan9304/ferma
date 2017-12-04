# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin.templatetags.admin_list import search_form
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView

from adverts.forms import CreateNewAdvertForm
from adverts.models import CreateNewAdvert, Media
from main.models import Banners, MainSlider


class AdvertListView(ListView):
    model = CreateNewAdvert
    context_object_name = 'all_ads'
    paginate_by = 10
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(AdvertListView, self).get_context_data(**kwargs)
        context['all_ads'] = sort_adds(CreateNewAdvert.objects.filter(is_active=True))
        context['slider'] = MainSlider.objects.all()
        if self.request.GET.get('category'):
            context['all_ads'] = sort_adds(
                CreateNewAdvert.objects.filter(is_active=True, categories=self.request.GET.get('category')))
        elif self.request.GET.get('search_words'):
            context['all_ads'] = sort_adds(CreateNewAdvert.objects.filter(text__icontains=self.request.GET.get('search_words')).all())
        return context


class AdCreate(CreateView):
    form_class = CreateNewAdvertForm
    model = CreateNewAdvert
    success_url = "/"
    template_name = 'new_advert.html'

    def get_context_data(self, **kwargs):
        context = super(AdCreate, self).get_context_data(**kwargs)
        context['slider'] = MainSlider.objects.all()
        return context


class AdDetail(DetailView):
    model = CreateNewAdvert
    template_name = 'one_ad_page.html'
    context_object_name = 'ad'


def copy_items(request):
    for i in range(10):
        obj = CreateNewAdvert.objects.get(pk=22)
        obj.pk = None
        obj.save()

    return JsonResponse(dict(sucess=True))


def sort_adds(obj):
    result = list()
    banner = Banners.objects.all()
    counter = 0
    adds_counter = 1
    if banner:
        for i in obj:
            if adds_counter % 4 != 0:
                result.append(i)
                adds_counter += 1
            else:
                if counter + 1 <= len(banner):
                    result.append(banner[counter])
                    adds_counter += 1
                    counter += 1
                else:
                    counter = 0
                    result.append(banner[counter])
                    counter += 1
                    adds_counter += 1
    else:
        result = obj
        # print sell_adds_list
    return result


@csrf_exempt
def upload_media(request):
    uploaded_files = list()
    files_count = len(request.FILES)
    for i in range(0, files_count):
        _file = request.FILES['file-' + str(i)]
        media = Media()
        media.media_file = _file
        media.save()
        uploaded_files.append({'id': media.id, 'url': media.media_file.url})
        print i
    return JsonResponse(dict(uploaded_files=uploaded_files))
