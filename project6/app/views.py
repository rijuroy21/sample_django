from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth


# Create your views here.

ad_us='admin'
ad_psw='admin@123'
def adminlogin(request):
    if request.method=='POST':
        adm_us=request.POST['username']
        adm_psw=request.POST['password']
        if ad_us==adm_us and ad_psw==adm_psw:
            return redirect(adminhome)
    return render(request,'admin/adminlogin.html')

def adminhome(request):
    emps=employee.objects.all()
    deps=department.objects.all()
    if request.method=='POST':
        dep=request.POST['d']
        deppk=department.objects.get(pk=dep)
        emps=employee.objects.filter(dname=deppk)
    return render(request,'admin/adminhomepage.html',{'deps':deps,'emps':emps})


def register(request):
    departments=department.objects.all()                               
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        dep=request.POST['d']
        current_dep=department.objects.get(pk=dep)
        data=employee.objects.create(name=name,email=email,username=username,password=password,dname=current_dep)
        data.save()
        return redirect(login)
    return render(request,'user/register.html',{'deps':departments})

    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        data=employee.objects.all()
        for i in data:
            if i.username==username and i.password==password:
                print(i)
                request.session['userlog']=i.username
                return redirect(home)
    return render(request,'user/login.html')

def home(request):
    if 'userlog' in request.session:
        emps=employee.objects.filter(username=request.session['userlog'])
        return render(request,'user/homepage.html',{'emps':emps})
    else:
        return redirect(login)

def update(request):
     if 'userlog' in request.session:
        emps=employee.objects.get(username=request.session['userlog'])
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']    
            emps=employee.objects.filter(username=request.session['userlog']).update(name=name,email=email)
            return redirect(home)
     return render(request,'user/update.html',{'emps':emps})
def logout(request):
    if 'userlog' in request.session:
        return redirect(login)
    else:
        return redirect(login)