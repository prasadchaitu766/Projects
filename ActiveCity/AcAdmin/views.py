import random
import re

from django.shortcuts import render
from .models import Add_Officer,Department
from AcLogin.models import Login

# Create your views here.
def AddOfficer(request):
    qs=Add_Officer.objects.all()
    qs1=Department.objects.all()
    for x in range(2):
        res2 = random.randint(1,100)
        id = "DCBA/ZYXW" + str(res2)
    return render(request,"AcAdmin/AdminRegistaration.html",{"officer":qs,"department":qs1,"id":id})


def departmentHome(request):

    dep=Department.objects.all()


    return render(request,"AcAdmin/Department.html",{"dep":dep})


def DepartmentDetails(request):
    Dep=request.POST.get("department")
    Department(name=Dep).save()
    dep = Department.objects.all()
    return render(request,"AcAdmin/Department.html",{"dep":dep,"message":"Successfully"+Dep+"Added"})


def sendACASMS(contact):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello Officer You have been Registread to Active City Application &language=english&route=p&numbers=" + contact
    headers = {
            'authorization': "WnE3TqV6AIv5qf8ir5PKnVjXxCzhCFCHasABU58gXRhO9JFqFluWZXvlbsv9",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
    # return render(request,"AcAdmin/AdminRegistaration.html",{"message":name+"Registred Successfully"})



def OfficerRegistaration(request):
    if request.method == "POST":
        idno = request.POST.get("id")
        name = request.POST.get("name")
        department = request.POST.get("dept")
        contact = request.POST.get("contact")
        image = request.FILES["image"]
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(idno,name,department,contact,image,username,password)

        message = sendACASMS(contact)
        import json
        d1 = json.loads(message)
        if d1["return"]:

            Add_Officer(id=idno, name=name, department_id=department, contact=contact, image=image,
                    username_id=username).save()
            Login(username=username, password=password, usertype="officer").save()
            qs = Department.objects.all()
            qs1 = Add_Officer.objects.all()
            return render(request, "AcAdmin/AdminRegistaration.html",
                          {"message": "Registered", "dept_data": qs, "officer_data": qs1})
        else:
            qs = Department.objects.all()
            qs1 = Add_Officer.objects.all()
            return render(request,  "AcAdmin/AdminRegistaration.html",
                          {"message": "Invalid Contact No", "dept_data": qs, "officer_data": qs1})




    # id=request.POST.get("id")
    # name=request.POST.get("name")
    # contact=request.POST.get("contact")
    # department=request.POST.get("department")
    # image=request.FILES["image"]
    # username=request.POST.get("username")
    # password=request.POST.get("password")
    # # password2=request.POST.get("password2")
    # c_no=Add_Officer.objects.values("contact")
    # contact_numbers=[]
    # for x in c_no:
    #     contact_numbers.append(x)
    # if contact in contact_numbers:
    #     return render(request,"AcAdmin/AdminRegistaration.html",{"Message":"This ContactNumber Already Used Please Use AnotherNumber"})
    # elif len(password)>8:
    #     return render(request,"AcAdmin/AdminRegistaration.html",{"Mesage":"Your Password Must Be More Than 8 characters"})
    # elif re.search('[0-9]',password) is None:
    #     return render(request,"AcAdmin/AdminRegistaration.html",{"Message":"Your Password Contains Atleast One Number."})
    # elif re.search('[a-z]',password) is None:
    #     return render(request,"AcAdmin/AdminRegistaration.html",{"Message":"Your Paasord Must Be Having One Lower CaseLetter"})
    # elif re.search('[A-Z]',password) is None:
    #     return render(request,"AcAdmin/AdminRegistaration.html",{"Message":"Your Paasord Must Be Having One Upper CaseLetter"})
    # else:
    #     import requests
    #
    #     Login(username=username,password=password,usertype="officer").save()
    #     Add_Officer(id=id,name=name,contact=contact,department_id=department,image=image,username_id=username).save()
    #     url = "https://www.fast2sms.com/dev/bulk"
    #     payload = "sender_id=FSTSMS&message=Hello Officer You have been Registread to Active City Application &language=english&route=p&numbers=" + contact
    #     headers = {
    #         'authorization': "WnE3TqV6AIv5qf8ir5PKnVjXxCzhCFCHasABU58gXRhO9JFqFluWZXvlbsv9",
    #         'Content-Type': "application/x-www-form-urlencoded",
    #         'Cache-Control': "no-cache",
    #     }
    #     response = requests.request("POST", url, data=payload, headers=headers)
    #
    # return render(request,"AcAdmin/AdminRegistaration.html",{"message":name+"Registred Successfully"})


def Dep_delete(request):
    Dep=request.GET.get("name")
    Department.objects.filter(name=Dep).delete()
    dep=Department.objects.all()
    return render(request,"AcAdmin/Department.html",{"dep":dep})


def Dep_update(request):
    DEP=request.GET.get("name")
    dep = Department.objects.all()
    return render(request,"AcAdmin/Department.html",{"dep":dep,"DEP":DEP})


def Update_Departmnet(request):
    d=request.POST.get("department")
    d1=request.POST.get("department1")
    Department.objects.filter(name=d1).update(name=d)
    dep = Department.objects.all()
    return render(request,"AcAdmin/Department.html",{"dep":dep})
