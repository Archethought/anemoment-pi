from django.shortcuts import render
from django.http import JsonResponse
import random
from django.utils import timezone
from datetime import timedelta

from .models import WindData


# Create your views here.
def graph(request):
    return render(request, 'anemoment/graph.html')


def wind_data(request):
    threshold = timezone.now() - timedelta(minutes=1)
    model_data = list(WindData.objects.filter(timestamp__gte=threshold).values())
    WindData.objects.create(
        x_speed=random.uniform(-1, 1),
        y_speed=random.uniform(-1, 1),
        z_speed=random.uniform(-1, 1),
    )
    return JsonResponse(model_data, safe=False)