from django.db import models

from AcAdmin.models import Department
from AcLogin.models import Login


class Citizen_Register(models.Model):
    Citizen_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    Address=models.TextField()
    City=models.TextField()
    image=models.ImageField(upload_to="Citizen/")
    username=models.ForeignKey(Login,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
class Complaints(models.Model):
    Complaint_id=models.AutoField(primary_key=True)
    Citizen_Id=models.ForeignKey(Citizen_Register,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    message=models.TextField()
    image=models.ImageField(upload_to="Complaints/")
    Complaint_registerDate=models.DateField()
    Status=models.CharField(max_length=20)
    Complaint_CLosingDate=models.DateField()
class Feedback(models.Model):
    fid=models.AutoField(primary_key=True)
    ComplaintId=models.ForeignKey(Complaints,on_delete=models.CASCADE)
    citizen_id=models.ForeignKey(Citizen_Register,on_delete=models.CASCADE)
    message=models.TextField()
    image=models.ImageField(upload_to="Feedback_Images/")
class OTP(models.Model):
    Contact=models.IntegerField(primary_key=True)
    OTP=models.CharField(max_length=6)
