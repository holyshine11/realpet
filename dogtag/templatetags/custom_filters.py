from django import template

register = template.Library()

@register.filter
def mask_last_four(value):
    return value[:-4] + '****'
