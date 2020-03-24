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


# Create your models here.
