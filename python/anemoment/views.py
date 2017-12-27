from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import WindData


# Create your views here.
def graph(request):
    return render(request, 'anemoment/graph.html')


def wind_data(request):
    DEFAULT_MINUTES_SHOWN = 2
    minutes_shown = request.GET.get("minutes_shown", DEFAULT_MINUTES_SHOWN)
    start_time = timezone.now() - timedelta(minutes=float(minutes_shown))
    model_data = list(WindData.objects.filter(timestamp__gte=start_time).values())
    return JsonResponse(model_data, safe=False)