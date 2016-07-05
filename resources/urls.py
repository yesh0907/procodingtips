from django.conf.urls import url

from . import views

app_name = 'resources'
urlpatterns = [
	url(r'^$', views.all_resources_and_groups, name="index"),
	url(r'^groups/$', views.all_groups, name="groups"),
	url(r'^groups/(?P<group_id>[0-9]+)', views.group_detail, name='group_detail'),
]