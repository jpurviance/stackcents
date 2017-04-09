from django.conf.urls import url

from . import views
from . import api

app_name = 'core'

urlpatterns = [url(r'^save_data/$', api.save_data, name="save_data"),
               url(r'^get_cpu_for_instance/(\S+)/$', api.get_cpu_for_instance, name="get_cpu_for_instance"),
               url(r'^get_instances_summary/$', api.get_instances_summary, name="get_instances_summary"),
               url(r'^$', views.dashboard, name="dashboard"),
               url(r'^ec2/$', views.ec2, name="ec2"),
               url(r'full_list/$', views.full_list, name="full_list"),
               url(r'^get_instance_details/$', api.get_instance_details, name="get_instance_details"),
               url(r'^get_instances/$', api.get_instances, name="get_instances"),
               url(r'^get_all_time_series/$', api.get_all_time_series, name="get_all_time_series"),
               url(r'^get_recommendation/$', api.get_recommendation, name="get_recommendation"),
               url(r'^get_time_series/$', api.get_time_series, name="get_time_series"),
               url(r'^get_script/$', api.get_script, name="get_script"),
               url(r'^everything/$', api.everything, name="everything")
               ]
