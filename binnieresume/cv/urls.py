from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^sitemap/$', views.sitemap, name='sitemap'),

]
