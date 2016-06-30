from django.conf.urls import url

from . import views

app_name = 'resources'
urlpatterns = [
	url(r'^$', views.all_resources_and_groups),
	url(r'^groups/$', views.all_groups),
	url(r'^categories/', views.all_groups),
	url(r'^groups/(?P<group_id>[0-9]+)', views.group_detail, name='group_detail'),
]