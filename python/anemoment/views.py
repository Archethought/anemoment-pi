from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import WindData

# Create your views here.
def graph(request):
    return render(request, 'anemoment/graph.html')

def wind_data(request):
    model_data = list(WindData.objects.all().values())
    return JsonResponse(model_data, safe=False)