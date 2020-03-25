<<<<<<< HEAD
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    profile_photo=CloudinaryField('images')
    bio=HTMLField()
    username = models.CharField(max_length=30,default='User')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
from django.db import models
import datetime as dt

class Neighbourhood(models.Model):
    name = models.CharField(max_length =60)
    location = models.CharField(max_length =60)
    occupants = models.CharField(max_length =60)
    # admin = models.ForeignKey(Admin)
    pub_date = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length =60)
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,)
    status = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)

class Business(models.Model):
    name = models.CharField(max_length =60)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,)




# Create your models here.
=======

>>>>>>> f43f7746606b0f90794783a828411cdf49829290
