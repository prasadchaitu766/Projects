
from django.shortcuts import render


def CampusDetails(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})


def Home(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})


def HomePage(request):
    type="home"
    return render(request,"index.html",{"type":type})
