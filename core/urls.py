from django.conf.urls import url

from . import views
from . import api

app_name = 'stackcents'



urlpatterns = [url(r'^echo/$', api.echo, name="echo")]