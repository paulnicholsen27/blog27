from django import template

register = template.Library()

@register.filter(name='shorten')
def shorten(content):
	#will show up to the first 500 characters of the post content
	if len(content) > 500:
		return content[:500] + '....' #+ <a href="/entry/{{post.id}}">(cont.)</a>
	else:
		return content