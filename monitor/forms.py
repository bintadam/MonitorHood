from django import forms
from .models import Neighbour, Post

# Create your forms here.

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ['user', 'name', 'description', 'location', 'population', 'image']
  

