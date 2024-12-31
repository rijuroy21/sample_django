from django.db import models

# Create your models here.

class teacher(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)

class UserUpload(models.Model):
    document = models.FileField()
    

    def __str__(self):
        return self.title