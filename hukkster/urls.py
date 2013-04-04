from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()



urlpatterns = patterns('blog.views',
	url(r'^$', 'main'),
	url(r'^(?P<username>\w{0,20})/$', 'main'),
	url(r'^entry/(?P<post_key>\d+)/$', 'post'), # links to single post by fk
    url(r'^createuser/$', 'create_user'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
