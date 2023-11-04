from django import template
import base64

register = template.Library()

@register.filter
def base64_encode(value):
    value_str = str(value)
    value_bytes = value_str.encode('utf-8')
    base64_bytes = base64.b64encode(value_bytes)
    return base64_bytes.decode('utf-8')
