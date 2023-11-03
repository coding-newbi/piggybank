from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"about.html")



        else:
            messages.info(request,"invalid user")

    return render(request,"login.html")
