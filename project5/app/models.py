from django.db import models

# Create your models here.
class user(models.Model):
    name=models.TextField()
    email=models.TextField()
    phone=models.TextField()
    username=models.TextField()
    password=models.TextField()
