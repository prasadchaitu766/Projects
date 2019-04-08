from AcLogin.models import Login
from django.db import models
from urllib3 import fields


class Department(models.Model):
    name=models.CharField(max_length=50)
class Add_Officer(models.Model):
    id=models.CharField(max_length=15,primary_key=True)
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=50)
    contact=models.IntegerField()
    image=models.ImageField(upload_to="Officer/")
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50,default=False)
