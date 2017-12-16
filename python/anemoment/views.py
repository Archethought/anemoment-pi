from django.shortcuts import render
from django.http import JsonResponse

from .models import WindData

# Create your views here.
def graph(request):
    return render(request, 'anemoment/graph.html')

def wind_data(request):
    data = WindData.objects.all().values('timestamp', 'speed')
    return JsonResponse(list(data), safe=False)