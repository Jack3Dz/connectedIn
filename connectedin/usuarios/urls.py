from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView
import django.contrib.auth.views

import app.forms
import app.views

urlpatterns = [
    # Examples:
	url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar')

]
