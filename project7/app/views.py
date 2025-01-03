from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def model_form_dis(request):
    data=model_form()
    if request.method=='POST':
        form=model_form(request.POST)
        if form.is_valid():
            form.save()
            print('successfull')
        else:
            print('error')
        return redirect(model_form_dis)
    return render(request,'teachers.html',{'data':data})


def upload(request):
    datas=UserUpload.objects.all()
    print(datas)
    if request.method=='POST':
        file=request.FILES['data']
        data=UserUpload.objects.create(document=file)
        data.save()
        return redirect(upload)
    return render(request,'upload.html',{'data':datas})


def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        data=User.objects.create_user(first_name=name,email=email,username=username,password=password)
        data.save()
        return redirect(login)
    return render(request,'user/register.html')

        

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # print(username,password)
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user:
            print(user)
            auth.login(request,user)
            return redirect(home)
    return render(request,'user/login.html')


def home(request):
    if '_auth_user_id' in request.session:
        return render(request,'user/home.html')
    else:
        return redirect(login)