from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,max_length=100)
    phone=models.IntegerField()

    def __str__ (self):
        return self.user.username


