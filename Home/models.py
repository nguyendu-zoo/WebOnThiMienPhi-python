from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    birthday = models.DateTimeField()
    date_create = models.DateTimeField(auto_now_add=True)
