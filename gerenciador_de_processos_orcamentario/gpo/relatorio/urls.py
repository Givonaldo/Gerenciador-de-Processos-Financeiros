from django.conf.urls import url
from gpo.relatorio.views import *

urlpatterns = [
    url(r'^relatorio/$', relatorio_view, name='relatorios_view'),
    url(r'^relatorio/formulario_interno$', relatorio_de_testes, name='formulario_diaria_interno')
]