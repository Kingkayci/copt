from django.db import models
from django.contrib.auth.models import User

class UploadedImage(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics/')

class UploadKYC(models.Model):
    card = models.ImageField(upload_to="profile_pics")
    imagePassport = models.ImageField(upload_to="profile_pics")
