import random
import re

from django.shortcuts import render, redirect

from AcLogin.models import Login
from.models import Citizen_Register,OTP

# Create your views here.
def CitizenComplaints(request):
    return render(request,"AcCitizen/Complaint.html")


def citizen_register(request):
    for x in range(2):
        id=random.randint(1,1000)
    return render(request,"AcCitizen/citizenRegistration.html",{"id":id})


def Register_Details(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    contact=request.POST.get("contact")
    address=request.POST.get("address")
    city=request.POST.get("city")
    image=request.FILES["image"]
    username=request.POST.get("username")
    password=request.POST.get("password")
    otp=name[0]+str(contact[-1]+contact[3])+username[2]+password[-2]
    if len(password) > 8:
        return render(request,"AcAdmin/AdminRegistaration.html",{"Mesage":"Your Password Must Be More Than 8 characters"})
    elif re.search('[0-9]',password) is None:
        return render(request,"AcAdmin/AdminRegistaration.html",{"Message":"Your Password Contains Atleast One Number."})
    elif re.search('[a-z]',password) is None:
        return render(request,"AcAdmin/AdminRegistaration.html",{"Message":"Your Paasord Must Be Having One Lower CaseLetter"})
    elif re.search('[A-Z]',password) is None:
        return render(request,"AcAdmin/AdminRegistaration.html",{"Message":"Your Paasord Must Be Having One Upper CaseLetter"})
    else:
        sendACASMS(contact, otp)
        OTP(Contact=contact,OTP=otp).save()
        Citizen_Register(Citizen_id=id,name=name,contact=contact,Address=address,City=city,image=image,username=username,password=password,status="pending").save()
        Login(username=username,password=password,usertype="citizen").save()
        return render(request,"AcCitizen/OtpValidate.html",{"name":name})
def sendACASMS(contact,otp):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello Citizen You have been Registread to Active City Application"+"Your Otp Is :"+otp+" &language=english&route=p&numbers=" + contact
    headers = {
            'authorization': "WnE3TqV6AIv5qf8ir5PKnVjXxCzhCFCHasABU58gXRhO9JFqFluWZXvlbsv9",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text


def Validations(request):
    contact=request.POST.get("contact")
    otp=request.POST.get("otp")
    name=request.POST.get("name")
    qs=OTP.objects.filter(Contact=contact,OTP=otp)

    if qs:
        Citizen_Register.objects.filter(contact=contact).update(status="Active")
        return render(request,"AcCitizen/home.html",{"name":name})
    else:
        return render(request,"AcCitizen/OtpValidate.html",{"messsage":"Invalid Otp"})


def citizen_profile(request):
    name=request.GET.get("name")
    qs=Citizen_Register.objects.filter(username=name)
    return render(request,"AcCitizen/updateprofile.html",{"qs":qs})


def Citizen_Logout(request):
    request.session['username']=False
    return redirect("main_page")