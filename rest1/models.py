from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

c_gender=[('male','Male'),('female','Female')]

# Register your models here.
class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    phone = models.CharField(max_length=10, blank=True)
    DOB = models.DateField(blank = True, null = True)
    gender = models.CharField(choices=c_gender, blank = True, null = True,max_length=10)
    image=models.ImageField(upload_to='images',null = True)



