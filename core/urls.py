from django.conf.urls import url

from . import views
from . import api

app_name = 'core'

urlpatterns = [url(r'^save_data/$', api.save_data, name="save_data"),
               url(r'^get_instances/$', api.get_instances, name="get_instances"),
               url(r'^get_cpu_for_instance/(\S+)/$', api.get_cpu_for_instance, name="get_cpu_for_instance"),
               url(r'^get_instances_summary/$', api.get_instances_summary, name="get_instances_summary"),
               url(r'^dashboard/$', views.dashboard, name="dashboard"),
               url(r'^get_instance_details/$', api.get_instance_details, name="get_instance_details")
               ]
