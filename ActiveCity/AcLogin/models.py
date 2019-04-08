from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=15)
