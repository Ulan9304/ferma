from django.conf.urls import url

from adverts.views import AdCreate, AdDetail, upload_media

urlpatterns = [
    url(r'^ad_create/$', AdCreate.as_view(), name='ad_create'),
    url(r'^view_more/(?P<pk>\d+)/$', AdDetail.as_view(), name='ad_detail'),
    url(r'^upload_media/$', upload_media, name='upload_media'),
]
