from django.db import models

from django import forms

gender=(('male','Male'),('female','Female'),('others','Others'))

class Selection(models.Model):
    Gender=models.CharField(max_length=10,choices=gender,default="male" )




