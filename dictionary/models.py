from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=70, null=True, blank=True)
    img = models.ImageField()
    facebook = models.CharField(max_length=70, null=True, blank=True )
    telegram = models.CharField(max_length=70, null=True, blank=True)
    instagram = models.CharField(max_length=70, null=True, blank=True)
    pinterest = models.CharField(max_length=70, null=True, blank=True)



class UploadImg(models.Model):
    img_title = models.CharField(max_length=150)
    img = models.FileField()
    def __str__(self):
        return self.img_title

