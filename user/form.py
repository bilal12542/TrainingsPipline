from django import forms
from server.models import ServerReservation


class AddReservation(forms.ModelForm):
    class Meta:
        model = ServerReservation
        fields = ['server_id', 'user_id', 'reservation_time', 'end_time']
