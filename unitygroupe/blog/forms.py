from . import models
from django.forms import ModelForm

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'website', 'message']
