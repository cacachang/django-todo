from django import template

register = template.Library()

@register.filter
def is_completed(status):
    return 'true' if status == 'Completed' else 'false'
