from django import forms
from models import Post, Comment
from django.db import models

class PostForm(forms.ModelForm):
	# title = models.CharField(max_length=255)
	# content = models.TextField()
	# created = models.DateTimeField(auto_now_add=True)
	# author = models.ForeignKey(User)
	text = models.TextField()

	class Meta:
		model = Post
		exclude = ['author', 'slug']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['post']