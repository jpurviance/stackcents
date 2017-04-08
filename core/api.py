from django.http import JsonResponse
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

@csrf_exempt
def echo(request):
    post = request.Post
    print(post)
    return HttpResponse(status=200)
