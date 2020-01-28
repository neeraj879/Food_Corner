from django.db import models
from django.utils import timezone
# Create your models here.

class UserAccount(models.Model):
    Name = models.CharField(max_length=30)
    username = models.EmailField()
    Mobile = models.IntegerField()
    Password = models.CharField(max_length=30)
    Created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return (self.Name)