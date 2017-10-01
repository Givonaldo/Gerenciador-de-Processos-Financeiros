from django.conf.urls import url
from gpo.core.views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^register/$', RegistrationView.as_view(), name="register"),

]
