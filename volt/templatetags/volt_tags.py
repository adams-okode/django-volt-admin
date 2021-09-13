import datetime
import urllib

from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.contrib.admin.utils import (display_for_field, display_for_value,
                                        get_fields_from_path, label_for_field,
                                        lookup_field)
from django.contrib.admin.views.main import (ALL_VAR, IS_POPUP_VAR, ORDER_VAR,
                                             PAGE_VAR, SEARCH_VAR)
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.template import Library
from django.template.loader import get_template
from django.templatetags.static import static
from django.urls import NoReverseMatch
from django.utils import formats, timezone
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import gettext as _

register = Library()


@register.simple_tag(name='active_section')
def active_section(request, value):
    # print(request.path)
    """Removes all values of arg from the given string"""
    for model in value['models']:
        if model['admin_url'] in urllib.parse.quote(request.path):
            return 'active'
    return ''


@register.simple_tag(name='volt_paginator_number')
def paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    # print(i, cl.paginator.num_pages)
    ELLIPSIS = _('…')
    if i == ELLIPSIS:
        return format_html('<li class="page-item disabled"><a class="page-link active">{}</a></li>', ELLIPSIS)
    elif i == cl.page_num:
        return format_html('<li class="page-item active"><a href="#" class="page-link active">{}</a></li>', i + 1)
    else:
        return format_html(
            '<li class="page-item {}"><a href="{}" class="page-link">{}</a></li>',
            mark_safe('disabled' if i == cl.paginator.num_pages else ''),
            cl.get_query_string({
                PAGE_VAR: i
            }),
            i + 1
        )
