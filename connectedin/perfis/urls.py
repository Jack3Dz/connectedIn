"""
Definition of urls for connectedin.
"""

from datetime import datetime
from django.conf.urls import url
from perfis import views
import django.contrib.auth.views

import app.forms
import app.views

urlpatterns = [
    # Examples:
	url(r'^$', views.index, name='index'),
	url(r'^perfis/(?P<perfil_id>\d+)$', views.perfis, name='perfis'),
	url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar')

]
