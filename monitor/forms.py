from django import forms
from .models import Neighbour, Profile, Post, Business

# Create your forms here.

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ['user', 'name', 'location', 'population']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'image', 'neighbourhood']				


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'neighbourhood','image']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['user', 'name', 'email', 'neighbourhood']				

  

