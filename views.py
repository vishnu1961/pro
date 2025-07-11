from django.shortcuts import render,redirect
from.models import*
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def register(request):
   log=Login()
   log.username=request.POST.get("username")
   log.password=request.POST.get("password")
   log.usertype="user"
   log.status="Approved"
   log.save() 

   obj=UserInfo()
   obj.name=request.POST.get("name")
   obj.address=request.POST.get("address")
   obj.phone_number=request.POST.get("phone_number")
   obj.email=request.POST.get("email")
   obj.login=log
   obj.save()
   messages.add_message(request,messages.INFO,'Registered successfully.')
   return redirect('registration')
#    return render(request,'success.html',{'name':name,'address':address})

def login_action(request):
    u=request.POST.get("username")
    p=request.POST.get("password")
    obj=authenticate(username=u,password=p)
    if obj is not None:
        if obj.is_superuser == 1:
            request.session['aname'] = u
            request.session['slogid'] = obj.id
            return redirect('admin_home')
        else:
            messages.add_message(request, messages.INFO,'Invalid user.')
            return redirect('login')
    else:
        messages.add_message(request, messages.INFO,'Invalid user.')
        return redirect('Login')
    
def admin_home(request):
        if 'aname' in request.session:
            return render(request, 'Master/index.html')
        else:
            return redirect('login')
        
def user_home(request):
        if 'aname' in request.session:
            return render(request, 'Master/index.html')
        else:
            return redirect('login')
        
def userlist(request):
        if 'aname' in request.session:
            data=UserInfo.objects.all()
            return render(request, 'Master/userlist.html',{'userdata':data})
        else:
            return redirect('login')
        
def addbook(request):
        if 'aname' in request.session:
            return render(request, 'Master/addbook.html')
        else:
            return redirect('login')
def booklist(request):
        if 'aname' in request.session:
            return render(request, 'Master/booklist.html')
        else:
            return redirect('login')