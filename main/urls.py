from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^hash_url/', views.hash_url, name="hash_url"),
    url(r'^check/', views.check, name="check"),
    url(r'^hash_url_redirect/(?P<url_id>[0-9]+)/$', views.hash_url_redirect, name="hash_url_redirect"),

]
