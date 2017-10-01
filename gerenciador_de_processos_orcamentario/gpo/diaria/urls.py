from django.conf.urls import url
from gpo.diaria.views import *

urlpatterns = [
    url(r'^diaria/add', diaria_add, name='diaria_add'),
    url(r'^diaria/diarias', listagem_diarias, name='diarias'),
    url(r'^diaria/', diaria, name='diaria'),
]
