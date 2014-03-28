from django.conf.urls import patterns, url, include
from frontend import views

urlpatterns = patterns('',\
    url(r'^/?$',
        views.index, name='index'),
    url(r'^portfolio/(?P<item>\d+)/?$',
        views.portfolio, name='portfolio'),
    url(r'^pages/(?P<page>.+)$',
        views.page, name='page'),
)

