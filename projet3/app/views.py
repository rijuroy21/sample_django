from django.shortcuts import render,redirect
adminun='Admin'
adminpas='123'
user=[]
def index(request):
    print(user)
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        email=request.POST['email']
        user.append({'username':username, 'password':password, 'name':name, 'email':email})
        print(user)
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        for i in user:
            if username==i['username'] and password==i['password']:
                print(i['name'])
            return redirect(home)
    return render(request,'index2.html')
def adminlogin(request):
    if request.method=='POST':
        adminun=request.POST['username']
        adminpas=request.POST['password']
        if adminun==adminun and adminpas==adminpas :
            return redirect(adminhome)
    return render(request,'adminlogin.html')    
def adminhome(request):
    return render(request,'adminhome.html',{'users':user})
def home(request):
    return render(request,'home.html')   