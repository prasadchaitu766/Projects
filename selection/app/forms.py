from django.forms import ModelForm
from .models import Selection
from django import forms
gender=[('male','Male'),('female','Female')]


class MySelection(ModelForm):
    class Meta:
        model = Selection
        fields = ['Gender']



