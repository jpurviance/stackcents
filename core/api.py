import collections
from django.http import JsonResponse
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def echo(request):
    post = request.POST
    print(dict(post))
    return HttpResponse(status=200)


countmap = collections.defaultdict(int)
@csrf_exempt
def count(request,number):
    countmap[number] += 1
    return JsonResponse({"Count" : countmap[number]})

