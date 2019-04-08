from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic import CreateView

from app.models import Selection
from .forms import MySelection


class CreateMyModelView(CreateView):
    model = Selection
    form_class = MySelection
    template_name = 'template.html'
    success_url = 'success.html'
