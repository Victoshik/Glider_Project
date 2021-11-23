from django import template
from gl.models import *

register = template.Library()


@register.inclusion_tag('list_events.html')
def show_events():
    event = Events.objects.all()
    return {'event': event}
