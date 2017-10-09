from django.conf.urls import url
from gpo.relatorio.views import *

urlpatterns = [
    url(r'^relatorio', relatorio_view, name='relatorios_view'),
]