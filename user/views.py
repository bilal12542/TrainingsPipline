import sys
from django.shortcuts import render, redirect
from .models import User
from server.models import ServerManagement
from django.http import HttpResponseRedirect
from .form import AddReservation
from server.models import ServerReservation

sys.path.append("..")
# Create your views here.


def index(request):
    return render(request, 'user/login/login.html', {})


def user_login(request):
    if request.method == 'POST':
        User_name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.empAuth_objects.get(User_name=User_name, password=password)
            if user is not None:
                return render(request, 'user/login/dashboard.html', {})
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(User_name, password))

                return redirect('/')
        except Exception as identifier:

            return redirect('/')

    else:
        return render(request, 'user/login/login.html')


def reservation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddReservation(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/dashboard/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddReservation()
    return render(request, 'user/login/reservation.html', {'form': form})


def book(request):
    return render(request, 'user/login/Book.html')


def dashboard(request):
    return render(request, 'user/login/dashboard.html')


def available_server(request):
    wal = ServerManagement.objects.all()
    dt = []
    for i in wal:
        dt += [
            {
                'servername': i.server_name,
                'ram': i.ram,
                'processor': i.processor,
                'available': i.enable
            }
        ]
    # json_obj_in_html = json2html.convert(json=dt)
    return render(request, 'user/login/available_server.html', {'ServerData': dt})
