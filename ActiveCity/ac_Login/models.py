from django.db import models

# Create your models here.
class Login_Details(models.Model):
    username=models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=10)
    user_type=models.CharField(max_length=10)
