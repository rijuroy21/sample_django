from django.db import models

# Create your models here.
class department(models.Model):
    dname=models.TextField()

    def __str__(self):
        return self.dname
class employee(models.Model):
    name=models.TextField()
    email=models.TextField()
    username=models.TextField()
    password=models.TextField()
    dname=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
