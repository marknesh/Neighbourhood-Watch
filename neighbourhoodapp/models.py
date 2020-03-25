from django.db import models
import datetime as dt

class Neighbourhood(models.Model):
    name = models.CharField(max_length =60)
    location = models.CharField(max_length =60)
    occupants = models.CharField(max_length =60)
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
