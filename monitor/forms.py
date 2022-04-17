from django import forms
from .models import Neighbour, Profile

# Create your forms here.

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ['user', 'name', 'description', 'location', 'population', 'image']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'image', 'neighbourhood']				
  

