from django.shortcuts import render

# Create your views here.
def moniter(request):
    return render(request, 'moniter.html', {})