from django.conf.urls import url

from . import views
from . import api

app_name = 'core'

urlpatterns = [url(r'^echo/$', api.echo, name="echo"),
               url(r'^count/(\d+)/$', api.count, name="count"),
               url(r'^get_instances/$', api.get_instances, name="get_instances"),
               url(r'^get_cpu_for_instance/(\S+)/$', api.get_cpu_for_instance, name="get_cpu_for_instance"),
               url(r'^get_instances_summary/$', api.get_instances_summary, name="get_instances_summary")
               ]
