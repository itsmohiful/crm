from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profile_picture/default_profile.jpg', upload_to='profile_picture')
    phone = models.CharField(max_length=15,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)


    def __str__(self):
        return f'{self.user.username} Profile'
