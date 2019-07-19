from django.shortcuts import render

# Create your views here.
def Sign_in(request):
    return render(request,"home.html",{"sign":"ok"})