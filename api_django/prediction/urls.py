from django.conf.urls import url
from .views import bike_list, bike_detail, predict

urlpatterns = [
    url(r'^predict/$', predict),
    url(r'^bikes/$', bike_list),
    url(r'^bike/(?P<pk>[0-9]+)/$', bike_detail),
]
