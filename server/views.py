from django.shortcuts import render
from .models import *
import json

# Create your views here.

def monitor(request):
    graph = []
    server = ServerManagement.objects.filter(enable=True)
    for var in server:
        result = CpuUsage.objects.filter(server_id=var)
        ls = []
        for a in result:
            ls.append(a.cpu)
        data = json.dumps(ls)
        graph.append(data)
    return render(request, 'monitor_page.html', {'result': graph})

def graph(request):
    return render(request, 'index.html')
