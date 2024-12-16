from django.shortcuts import render,redirect
from .models import *

# Create your views here.
ad_us='admin'
ad_psw='admin@123'
def adminlogin(request):
    if request.method=='POST':
        adm_us=request.POST['username']
        adm_psw=request.POST['password']
        if ad_us==adm_us and ad_psw==adm_psw:
            return redirect(adminhome)
    return render(request,'Admin/adminlogin.html')
def adminhome(request):
    return render(request,'Admin/adminhomepage.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        data=user.objects.create(name=name,email=email,phoneno=phone,username=username,passwword=password)
        data.save()
    return render(request,'User/register.html')
        
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        data=user.objects.all()
        for i in data:
            if i.username==username and i.passwword==password:
                request.session['userlog']=i.username
                return redirect(home)
    return render(request,'User/login.html')
def home(request):
    if 'userlog' in request.session:
        return render(request,'User/homepage.html')
    else:
        return redirect(login)
    
def logout(request):
    if 'userlog' in request.session:
        del request.session['userlog']
        return redirect(login)
    else:
        return redirect(login)
    
