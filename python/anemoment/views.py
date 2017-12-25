from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import WindData


# Create your views here.
def graph(request):
    return render(request, 'anemoment/graph.html')


def wind_data(request):
    DEFAULT_START_TIME = timezone.now() - timedelta(minutes=2)
    DEFAULT_END_TIME = timezone.now()
    start_time = request.GET.get("start_time", DEFAULT_START_TIME)
    end_time = request.GET.get("end_time", DEFAULT_END_TIME)
    model_data = list(WindData.objects.filter(timestamp__gte=start_time, timestamp__lte=end_time).values())
    return JsonResponse(model_data, safe=False)