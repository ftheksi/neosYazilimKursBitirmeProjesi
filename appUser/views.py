from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def registerUser(request):
    
    if request.method == "POST":
        name=request.POST.get("name")
        surname=request.POST.get("surname")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        harfup=False
        harfnum=False
        if password1==password2:
            
            for harf in password1:
                if harf.isupper():
                    harfup=True
                if harf.isnumeric():
                    harfnum=True
            
            if harfup and len(password1)>=6 and harfnum:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():

                        user=User.objects.create_user(username=username,password=password1,email=email,first_name=name,last_name=surname)

                        user.save()
                        return redirect('loginUser')
                    else:
                        messages.warning(request,"Bu mail zaten kullanılıyor!")
                        return redirect('registerUser')
                else:
                        messages.warning(request,"Bu kullanıcı adı başkası tarafından kullanılıyor!")
                        return redirect('registerUser')
            else:
                        messages.warning(request,"Şifrede en az 1 tane büyük harf olmalı!")
                        messages.warning(request,"Şifrede en az 1 tane rakam olmalı!")
                        messages.warning(request,"Şifreniz en az 6 karakterden oluşmalı!")
                        return redirect('registerUser')
        else:
                        messages.warning(request,"Şifreler aynı değil!")
                        return redirect('registerUser')

    return render(request,'user/register.html')


def loginUser(request):

    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        harfet=False
        for harf in username:
             if harf=="@":
                  harfet=True
        if username[-4:]==".com":
            try:
                user=User.objects.get(email=username)
                username=user.username
            except:
                    messages.warning(request,"Email kayıtlı değil!")
                    return redirect('loginUser')



        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('homePage')
        else:
            messages.warning(request,"Kullanıcı Adı veya şifre hatalı!")
            return redirect('loginUser')
    return render(request,'user/login.html')

def logoutUser(request):
    logout(request)
    return redirect('homePage')



