from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('available-server/server-reservation/', views.reservation, name='reservation'),
    path('available-server/Book/', views.book, name='Book'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('available-server/', views.available_server, name='available-server'),
    path('available-server/Booki/', views.upload, name='Booki'),
    path('Booki/', views.upload, name='requestdata')

]
