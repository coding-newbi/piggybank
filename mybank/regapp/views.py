from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')

            else:
                   user=User.objects.create_user(username=username,password=password)
                   user.save();

                   print("user created")
                   return redirect('login')

        else:
             messages .info(request," password mismatch found")
             return redirect('register')
        return redirect('/')
    return render(request,"reg.html")