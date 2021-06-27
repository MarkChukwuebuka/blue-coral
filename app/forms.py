from django import forms
from django.forms import ModelForm
from .models import * 

from django.contrib.auth import get_user_model

class AdForm(forms.ModelForm):


    class Meta:
        model = Property
        fields = '__all__'
        # ['description', 'price', 'property_type', 'floors', 'youtube_link', 'infrastructure_plan', 'apartment_layout', 'address', 'house_type', 'living_space', 'no_of_floors', 'bedrooms', 'ftsq']



class UpdateForm(forms.ModelForm):
    

    class Meta:
        model = Property
        fields = '__all__'
        # ['description', 'price', 'property_type', 'floors', 'youtube_link', 'infrastructure_plan', 'apartment_layout', 'address', 'house_type', 'living_space', 'no_of_floors', 'bedrooms', 'ftsq']