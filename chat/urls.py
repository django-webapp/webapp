from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chat/$', views.index1, name='index1'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]
