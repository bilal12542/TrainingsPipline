from django import forms
from server.models import ServerReservation


class AddReservation(forms.ModelForm):
    class Meta:
        model = ServerReservation
        fields = ['server_id', 'user_id', 'reservation_time', 'end_time']
        # widgets = {'server_id': forms.HiddenInput(), 'user_id':forms.HiddenInput()}
