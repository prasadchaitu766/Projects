from django.http import HttpResponse
from django.shortcuts import render, redirect
from AcAdmin.models import *
from AcLogin.models import Login

# Create your views here.
def LoginCheck(request):
    username=request.POST.get("Username")
    password=request.POST.get("Password")
    type=request.POST.get("Type")
    print(username,password,type)
    qs=Login.objects.filter(username=username,password=password,usertype=type)

    if qs:
        if type=="admin":
            return redirect("admin_home")
            # return HttpResponse("admin login")
        elif type=="officer":
            return redirect("officer_home")
            # return HttpResponse("OfficerLogin")
        else:
            return redirect("citizen_home")
            # return HttpResponse("CitizenLogin")

    else:
        if type=="admin":
            return HttpResponse("admin Invalid")
        elif type=="officer":
            return HttpResponse("Officer Invalid")
        else:
            return HttpResponse("Citizen Invalid")
