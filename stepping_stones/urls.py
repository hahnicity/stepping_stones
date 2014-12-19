from django.conf.urls import patterns, url

from stepping_stones import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
