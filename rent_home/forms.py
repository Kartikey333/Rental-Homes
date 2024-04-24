from django.forms import ModelForm
from django import forms
from .models import Room, House


class HouseForm(ModelForm):

    class Meta:
        model = House
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'latitude' : forms.NumberInput(attrs={'id': 'lat'}),
            'longitude': forms.NumberInput(attrs={'id': 'long'})
        }

class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['house']
        widgets = {
            'budget_range': forms.Select(attrs={'id': 'budget-range'}),
        }

