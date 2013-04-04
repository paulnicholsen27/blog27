
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User 

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog.views.main', args=[self.slug])


class Comment(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.body[:60]))

