# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def dashboard(request):
    return (render(request, "core/dashbard.html", {}))


def ec2(request):
    ec2_id = request.GET.get("id", "-1")
    context = {"id": ec2_id}
    return render(request, "core/ec2.html", context)
