from django.db import models

# Create your models here.
from ac_Admin.models import Department
from ac_Login.models import Login_Details


class User_Registration(models.Model):
    citizen_id = models.AutoField(primary_key=True)
    citizen_name = models.CharField(max_length=20)
    citizen_contact = models.IntegerField()
    citizen_Address = models.TextField()
    citizen_city = models.CharField(max_length=20)
    citizen_image = models.ImageField(upload_to='register/')
    citizen_username = models.ForeignKey(Login_Details, on_delete=models.CASCADE)

class complaint(models.Model):
    citizen_id=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
    complaint_id=models.IntegerField(primary_key=True)
    department_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    complaint_messgae=models.TextField()
    complaint_image=models.ImageField(upload_to='complaints/')
    Date_of_Register=models.DateField()
    complaint_status=models.CharField(max_length=20)
    Date_of_Close=models.DateField()

class Feedback(models.Model):
    complaintid=models.ForeignKey(complaint,on_delete=models.CASCADE)
    citizenid=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
    msg=models.TextField()
    image=models.ImageField(upload_to='feedback/')
    feedbackid=models.AutoField(primary_key=True)
