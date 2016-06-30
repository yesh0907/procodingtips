from django.conf.urls import url

from . import views

app_name = 'tips'
urlpatterns = [
	url(r'^$', views.all_tip_list),
	url(r'^series/$', views.all_series_list),
	url(r'^tips/', views.all_tip_list),
	url(r'^series/(?P<pk>[0-9]+)/', views.all_tips_in_series, name='series_detail'),
]