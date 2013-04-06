from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'thestar.views.home', name='home'),
    # url(r'^my_first_app/', include('my_first_app.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
