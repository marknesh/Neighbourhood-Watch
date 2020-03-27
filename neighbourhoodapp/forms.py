from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

from .models import Post,Neighbourhood,Profile
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=200, help_text='Required')
    last_name = forms.CharField(max_length=200, help_text='Required')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, )
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1', 'password2')




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'user']
        widgets = {
            'neighbourhood': forms.Select,
        }



class postForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('updates','image',)


class neighbourhoodform(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        fields=('name','location','occupants')
