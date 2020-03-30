
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db import models
import datetime as dt


class Neighbourhood(models.Model):
    name = models.CharField(max_length =60)
    location = models.CharField(max_length =60)
    occupants = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
         self.save()


    @classmethod
    def allimages(cls):
        images = cls.objects.all()
        return images

    class Meta:
        ordering = ['name']



class Profile(models.Model):
    profile_photo=CloudinaryField('images')
    bio=HTMLField()
    username = models.CharField(max_length=30,default='User')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Post(models.Model):
    image = CloudinaryField('image',null=True)
    updates=models.CharField(max_length=300)
    neighbourhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.updates

    def save_comment(self):
        '''
        method that save a comment on an image
        '''
        self.save()


class Users(models.Model):
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

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()


    @classmethod

    def findbusiness(cls,name):
        foundbusiness=cls.objects.filter(name__icontains=name).all()
        return foundbusiness


# Create your models here.
