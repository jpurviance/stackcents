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
    print(ec2.stats)
    return json.loads(ec2.stats)
