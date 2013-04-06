from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^vote/', 'thestar.views.vote', name='vote'),
)
