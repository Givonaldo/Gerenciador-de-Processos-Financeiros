from django.conf.urls import url
from gpo.diaria.views import *

urlpatterns = [
    url(r'^diaria/add/', diaria_add, name='diaria_add'),
    url(r'diaria/gerar_capa/$', gerar_capa, name='gerar_capa'),
    url(r'diaria/gerar_memorando/$', gerar_memorando, name='gerar_memorando'),
    url(r'diaria/gerar_relatorio/$', gerar_relatorio, name='gerar_relatorio'),
    url(r'^diaria/diarias', listagem_diarias, name='diarias'),
    url(r'^diaria/', diaria, name='diaria'),
]
