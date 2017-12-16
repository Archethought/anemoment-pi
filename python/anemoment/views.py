from django.shortcuts import render

from .models import WindData

# Create your views here.
def graph(request):
    return render(request, 'anemoment/graph.html')

def wind_data(request):
    pass