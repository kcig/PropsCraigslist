from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.props_list, name='props_list'),
]