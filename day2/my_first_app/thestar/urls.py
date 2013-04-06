from django.conf.urls import patterns, include, url
from thestar.views import CompetitorAPI

urlpatterns = patterns('',
    url(r'^vote/', 'thestar.views.vote', name='vote'),
    url(r'^competitors/', CompetitorAPI.as_view(), name='competitors_api'),
)
