from django.shortcuts import render,redirect
from myappfile.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')
def signupuser(request):
    if request.method == 'POST':
        username=request.POST['user_name']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if User.objects.filter(username=username).exists():
            messages.success(request,'this username is already taken')
            return redirect('/signupuser')
        if len(username) > 10:
            return redirect('/signupuser')
        if pass1 != pass2:
            return redirect('/signupuser')
        myuser=User.objects.create_user(username=username,email=email,password=pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save();
        print('success........')
        return redirect('/loginuser')
    else:
        return render(request,'signupuser.html')
def loginuser(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
            print('login successful........')
        else:
            return redirect('/loginuser')
    else:    
        return render(request,'loginuser.html')
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        messages.success(request,"your message has been sent")
    return render(request,'contactus.html')
def aboutus(request):
    return render(request,'aboutus.html')
def logoutuser(request):
    auth.logout(request)
    print('successfully logout')
    return redirect('/')

