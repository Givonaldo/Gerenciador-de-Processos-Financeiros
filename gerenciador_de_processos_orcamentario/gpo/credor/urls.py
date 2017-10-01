from django.conf.urls import url
from gpo.credor.views import *

urlpatterns = [
    url(r'^credor/addservidor/', credor_servido_add, name='credor_servido_add'),
    url(r'^credor/addfornecedor/', credor_fornecedor_add, name='credor_fornecedor_add'),
    url(r'^credor/', credor, name='credor'),
]
