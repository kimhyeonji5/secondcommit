from django.conf.urls import url
from django import template
import re

register = template.Library()

@register.filter
def add_link(value):
    main_text = value.main_text
    tags = value.tag_set.all()

    for tag in tags:
        main_text = re.sub(r'\#'+tag.tag_name+r'\b', '<a href="/myApp/explore/tags/'+tag.tag_name+'">#'+tag.tag_name+'</a>', main_text)
    return main_text