from django.conf.urls import url

from . import views
from . import api

app_name = 'core'

urlpatterns = [
    url(r'^echo/$', api.echo, name="echo"),

    url(r'^dashboard/$', views.dashboard, name="dashboard")
]
