from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='name'),
    path('login', views.user_login, name='login'),
    path('server-reservation', views.reservation, name='reservation'),
    path('Book', views.book, name='Book'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('available-server/', views.available_server, name='available-server'),
    path('Booki', views.upload , name='requestdata')
]
