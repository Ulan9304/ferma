from django.contrib import admin

# Register your models here.
from adverts.models import CreateNewAdvert, Media

admin.site.register(CreateNewAdvert)
admin.site.register(Media)