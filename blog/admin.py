from django.contrib import admin

from models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'content'[:50], 'published', 'created', 'author')
	search_fields = ['title', 'content']
	ordering = ['-created']
	list_per_page = 10
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)

    