from django.conf.urls import patterns, url, include


urlpatterns = patterns('shortener.views',
	url(r'^sembed$', 'userview', name='userview'),
    url(r'^$', 'index', name='index'),
    url(r'^info/(?P<base62_id>\w+)$', 'info', name='info'),
    url(r'^submit/$', 'submit', name='submit'),
    url(r'^(?P<base62_id>\w+)$', 'follow', name='follow'),
    url(r'^[\!](?P<base62_id>\w+)$', 'info', name='info'),
)
