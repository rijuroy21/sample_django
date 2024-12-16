from django.db import models

# Create your models here.

class user(models.Model):
    username=models.TextField()
    passwword=models.TextField()
    name=models.TextField()
    email=models.TextField()
    phoneno=models.TextField()
   