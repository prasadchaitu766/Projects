from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AcAdmin.models import *
from AcLogin.models import Login
from AcCitizen.models import Citizen_Register

# Create your views here.
def LoginCheck(request):
    username=request.POST.get("Username")
    password=request.POST.get("Password")
    type=request.POST.get("Type")

    qs=Login.objects.filter(username=username,password=password,usertype=type)

    if qs:
        if type=="admin":
            return render(request,"AcAdmin/admin_home.html")
            # return HttpResponse("admin login")
        elif type=="officer":
            return render(request, "AcOfficer/home.html",{"name":username})
            # return HttpResponse("OfficerLogin")
        else:
            qs=Citizen_Register.objects.filter(username=username)
            if qs[0].status == 'Active':
                request.session['Citizen_id'] = qs[0].Citizen_id
                request.session['username'] = username
                return render(request,"AcCitizen/home.html",{"name":username})
            else:
                messages.error(request, "Please Validate Your OTP")
                return redirect('citizen_index')

            # return HttpResponse("CitizenLogin")

    else:
        if type=="admin":
            return HttpResponse("admin Invalid")
        elif type=="officer":
            return HttpResponse("Officer Invalid")
        else:
            return HttpResponse("Citizen Invalid")
