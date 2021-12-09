from django import forms
from server.models import ServerReservation


class AddReservation(forms.ModelForm):
    class Meta:
        model = ServerReservation
        fields = ['server_id', 'user_id', 'reservation_time', 'end_time']
    # user_name = forms.CharField(label='Your username', max_length=100)
    # server_name = forms.CharField(label='server name', max_length=100)
    # reservation_time = forms.DateTimeField(label='Reserve Time')
    # duration = forms.IntegerField(max_value=3, label='Enter number of hours')
