from django import forms
from django.forms import ModelForm

from . models import ReceiverShipCase



class ReceiverShipCaseForm(forms.ModelForm):
    
    class Meta:
        model = ReceiverShipCase
        fields = ['title', 'court', 'receiver', 'status']