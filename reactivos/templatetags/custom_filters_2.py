from django import template
from os.path import basename

register = template.Library()

@register.filter(name='filename')
def filename(value):
    return basename(value)
