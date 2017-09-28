from django.conf.urls import url
from gpo.core.views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^credor/', credor, name='credor'),
    url(r'^credor/add-servidor', credorServidoAdd, name='credor-servidor'),
    url(r'^diaria/add', diaria_add, name='diaria_add'),
    url(r'^diaria/', diaria, name='diaria'),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),

]
