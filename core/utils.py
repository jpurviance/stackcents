import collections
from django.http import JsonResponse
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from models import EC2
from django.utils import six

import json


def get_cpu(instance):
    this_instance = get_all().filter(name=instance).first()
    if this_instance is not None:
        return this_instance['cpu']
    else:
        return None


def get_all():
    return EC2.objects.all()


def get_json(ec2):
    return json.loads(ec2.stats)


def get_cpu_timeseries(instance):
    data = get_json(instance)
    all_cpus = list(sorted(data['cpu'], key=lambda x: x['index']))
    return [cpu['load_avg_1'] for cpu in all_cpus]


def get_all_cpu_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [get_cpu_timeseries(data) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(sum(lll) / float(len(lll)))
    return ll
