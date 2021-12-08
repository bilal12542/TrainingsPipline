from django.shortcuts import render


# Create your views here.

def monitor(request):
    return render(request, 'monitor_page.html', {})
