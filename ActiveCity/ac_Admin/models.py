from django.db import models

# Create your models here.
from ac_Login.models import Login_Details


class Department(models.Model):
    dept_name=models.CharField(primary_key=True,max_length=25)

class Officer(models.Model):
    officer_idno=models.AutoField(primary_key=True)
    officer_name=models.CharField(max_length=20)
    officer_contact=models.IntegerField()
    officer_user=models.ForeignKey(Login_Details,on_delete=models.CASCADE)
    officer_image=models.ImageField(upload_to='officer/')
    officer_department=models.ForeignKey(Department,on_delete=models.CASCADE)