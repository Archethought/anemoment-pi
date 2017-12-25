from django.shortcuts import render
from django.http import JsonResponse
import random
from django.utils import timezone
from datetime import timedelta
from .parser import Parser
from .models import WindData


# Create your views here.
def graph(request):
    return render(request, 'anemoment/graph.html')


def wind_data(request):
    threshold = timezone.now() - timedelta(minutes=1)
    model_data = list(WindData.objects.filter(timestamp__gte=threshold).values())
    return JsonResponse(model_data, safe=False)