from typing import ValuesView
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import StudentRegistration
from .models import User
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy

# for add new data and sho
def base1(request):
    if request.method =='GET':
        return render(request,'enroll/base1.html')
        #return HttpResponseRedirect('/')
        #context_object_name = 'base1'
        #template_name = 'enroll/base1.html'

def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg= User(name=nm,email=em,password=pw)
            reg.save()
            fm= StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})
#to update
def update_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html', {'form':id})



#to delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')