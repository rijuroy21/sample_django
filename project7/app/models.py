from django.db import models

# Create your models here.

class teacher(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)

class UserUpload(models.Model):
    document = models.FileField()

class User(models.Model):
    name=models.TextField()
    email=models.TextField()
    username=models.TextField()
    password=models.TextField()
    document=models.ForeignKey(UserUpload,on_delete=models.CASCADE)

    

