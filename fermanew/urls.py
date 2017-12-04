"""fermanew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from adverts.views import AdvertListView, copy_items
from companies.views import CompaniesListView
from fermanew import settings
from news.views import NewsListView

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    # url(r'^search/', include('jet.urls', 'jet')),
    url(r'^ad/', include('adverts.urls', namespace='ad')),
    url(r'^$', AdvertListView.as_view(), name='main'),
    url(r'^copy_items/', copy_items, name='copy_items'),
    url(r'^news/', NewsListView.as_view(), name='news'),
    url(r'^companies/', CompaniesListView.as_view(), name='companies'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^search_results/$', AdvertListView.as_view, name='search')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
