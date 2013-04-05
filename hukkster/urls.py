from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()



urlpatterns = patterns('blog.views',
	url(r'^$', 'main'),
	url(r'^entry/(?P<pk>\d+)/$', 'post'), # links to single post by pk
    url(r'^create_user/$', 'create_user'),
    url(r"^add_comment/(\d+)/$", "add_comment"),
    url(r'^logout/', 'log_out'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<username>\w{0,20})/$', 'main'), #must go last--will try to match anything to username

)
