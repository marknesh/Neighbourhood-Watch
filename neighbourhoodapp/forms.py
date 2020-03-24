from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class ProfileUpdateForm(forms.Form):
    '''
    classs that creates profile update form
    '''
    username = forms.CharField(label='Username',max_length = 30)
    profile_photo = forms.ImageField(label = 'Profile Photo')
    bio = forms.CharField(label='Bio',max_length=500)