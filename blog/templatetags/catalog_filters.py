from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='shorten')
def shorten(content, post_id):
    #will show up to the first 500 characters of the post content
    if len(content) > 500:
        output = "{0}... <a href='/entry/{1}'>(cont.)</a>".format(content[:500], post_id)
    else:
        output = "{0}".format(content)

    return mark_safe(output)