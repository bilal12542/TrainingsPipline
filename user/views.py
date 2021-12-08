from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#
# def index(request):
#     return render(request,'user/landing/landingpage.html',{})


def index(request):
    return render(request,'user/login/login.html', {})


def user_login(request):
    if request.method == 'POST':
        User_name = request.POST.get('username')
        password = request.POST.get('password')
        print(User_name,password)
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
