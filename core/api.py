import collections
from django.http import JsonResponse
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from models import EC2
from django.utils import six
from utils import EC2, get_json, get_all, get_cpu
import json


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            id = json_data['id']
            try:
                instance = EC2.objects.get(name=id)
                instance.stats = request.body
            except EC2.DoesNotExist:
                instance = EC2(name=id, stats=request.body)
            instance.save()
        except KeyError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


# API GETS
@csrf_exempt
def get_instances(request):
    instances = get_all()
    l = [e.name for e in instances]
    return JsonResponse({"instances": l})


@csrf_exempt
def get_all_cpu(request):
    instances = get_all()
    l = []
    for instance in instances:
        l.append(get_cpu(instance))
    return JsonResponse({"all_cpu": l})


@csrf_exempt
def get_instances_summary(request):
    all_data = (get_json(ec2) for ec2 in get_all())
    l = []
    for data in all_data:
        t = {'id': data['id'],
             'cpu': data['cpu']['load_avg']['1_min'] * 100,
             'memory': (data['mem']['used'] / data['mem']['total']) * 100,
             'network': 100000,
             'storage': data['storage']['percent']
             }
        l.append(t)
    return JsonResponse({"total": l})


@csrf_exempt
def get_cpu_for_instance(request, instance):
    i = get_cpu(instance)
    if i:
        return JsonResponse(i)
    else:
        return HttpResponse(status=404)
