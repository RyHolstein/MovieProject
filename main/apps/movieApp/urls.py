from django.conf.urls import url, include
from . import views


urlpatterns = {
    url(r'^movie/(?P<id>\d+)$', views.movie_page),
    url(r'^people/(?P<id>\d+)', views.cast_page)

}
