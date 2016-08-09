from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'snippets'
urlpatterns = [
	url(r'^snippets/$', views.SnippetList.as_view(), name='snippet_list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
