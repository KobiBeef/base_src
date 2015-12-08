from . import views
from django.conf.urls import patterns, url, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns


snippet_list = views.SnippetViewSet.as_view({
	'get': 'list',
	'post': 'create',
})

snippet_detail = views.SnippetViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy',
})

snippet_highlight = views.SnippetViewSet.as_view({
	'get': 'highlight',
}, renderer_classes = [renderers.StaticHTMLRenderer])

user_list = views.UserViewSet.as_view({
	'get': 'list',
})

user_detail = views.UserViewSet.as_view({
	'get': 'retrieve',
})


urlpatterns = patterns('',
	url(r'^$', views.api_root,),
	url(r'^detail/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
	url(r'^list/$', snippet_list, name='snippet-list'),
	url(r'^test/$', views.SnippetListView.as_view(), name="test"),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
	url(r'^users/$', user_list, name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)