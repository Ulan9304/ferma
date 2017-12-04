from django import template

from adverts.models import CreateNewAdvert
from adverts.views import sort_adds

register = template.Library()


@register.assignment_tag
def ads_types(type):
    result = sort_adds(CreateNewAdvert.objects.filter(is_active=True, advert_type=type))
    return result


register.filter('ads_types', ads_types)
