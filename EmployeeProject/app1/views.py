from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from app1.forms import RegisterForm
from django.http import HttpResponse

def index(request):

    return render(request,'index.html')

def registration(request):
    if request.method=='POST':
        # print(request.POST)
        data = RegisterForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("Data added successfully !!!")

    data = RegisterForm
    return render(request,'registration.html',{'form':data})