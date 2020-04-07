import django_filters
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from .models import Iris
from .serializer import IrisSerializer
from .forms import IrisForm
import json
import requests as rq

@api_view(['GET', 'POST'])
def index(request):
    result = None
    if request.method == 'POST':
        api_head = {
            'Content-Type': 'application/json',
        }

        payload = {
            "sepal_length": float(request.POST.get("sepal_length")),
            "sepal_width": float(request.POST.get("sepal_width")),
            "petal_length": float(request.POST.get("petal_length")),
            "petal_width": float(request.POST.get("petal_width"))
        }
        result = rq.post("http://192.168.100.100:5000/predict/", json.dumps(payload), headers=api_head)
        result = result.json()["result"]
        return render(request, 'index.html', {'form': IrisForm(), 'result': result})
    return render(request, 'index.html', {'form': IrisForm()})

class IrisViewSet(viewsets.ModelViewSet):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer
