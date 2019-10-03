from . import models
from django.forms import ModelForm

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'number', 'date_from','date_to', 'yatcht', 'email', 'phone_number', 'note']
