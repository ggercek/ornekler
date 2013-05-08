from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from socketio import sdjango

sdjango.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.views.index'),
    url(r'^socket\.io', include(sdjango.urls)),
)
urlpatterns += staticfiles_urlpatterns()