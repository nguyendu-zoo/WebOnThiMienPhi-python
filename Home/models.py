from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=15)
    Email = models.EmailField()
    SDT = models.CharField(max_length=12)
    NgaySinh = models.DateTimeField()
    NgayTao = models.DateTimeField(auto_now_add=True)
