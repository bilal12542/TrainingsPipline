import sys
from django.shortcuts import render, redirect
from server.models import ServerManagement
from .form import AddReservation
from django.contrib import messages
from server.models import ServerReservation
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .client import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# parentdir = Path(os.getcwd())
#
# sys.path.append("..")


# Create your views here.

def deletezip():
    for f in Path(os.path.join(parentdir, 'media')).glob('*.zip'):
        try:
            f.unlink()
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def upload(request):
    if request.method == "POST":
        if os.listdir(os.path.join(parentdir, 'media')):
            deletezip()
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        internal_id = request.POST.get('dataUpload')
        # print(internal_id)
        SendFile(internal_id)

    return render(request, 'user/login/dashboard.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, "Successfully Login with username: " + username)
                login(request, user)
                return redirect('dashboard')

            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))

                return redirect('/')
        except Exception as identifier:
            print(identifier)
            return redirect('/')

    else:
        return render(request, 'user/login/login.html')


def reservation(request):
    context = {}
    if request.POST.get('server'):
        request.session['server'] = request.POST.get('server')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        context['form'] = AddReservation(request.POST)
        # print(context['form'].data['server_id'])
        # check whether it's valid:
        # context['form'].fields['server_id'].initial = context['server_id']

        if context['form'].is_valid():
            del request.session['server']
            # process the data in form.cleaned_data as required
            # ...
            context['form'].save()
            # redirect to a new URL:
            return redirect('dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        context['form'] = AddReservation()
    return render(request, 'user/login/reservation.html', context)


def book(request):
    if request.method == 'POST':
        internal = request.POST.get('internal-id')

    return render(request, 'user/login/booked.html', {'internal_id': internal})


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'user/login/dashboard.html')


@login_required(login_url="login")
def available_server(request):
    server_res = ServerManagement.objects.all()
    dt = []
    for i in server_res:
        dt += [
            {
                'servername': i.server_name,
                'ram': i.ram,
                'processor': i.processor,
                'available': i.enable,
                'server_id': i.id
            }
        ]
    return render(request, 'user/login/available_server.html', {'ServerData': dt})


def logout_user(request):
    logout(request)
    return redirect('login')
