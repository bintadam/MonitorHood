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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'neighbourhood', 'image']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['user', 'name', 'description', 'neighbourhood']				

  

