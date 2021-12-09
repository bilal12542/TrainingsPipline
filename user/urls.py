

from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='name'),
    path('Server', views.user_login , name='login'),
    path('ServerReservation' , views.reservation, name='reservation' ),
    path('Book' ,views.book , name='Book' )
]
