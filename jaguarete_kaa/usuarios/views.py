
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import perfil

from django.db.utils import IntegrityError

from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect("home")
        else:
            return render(request,'./login/permiso.html',{'error':'invalid'})

    return render(request,"./login/permiso.html",context={'perfil':perfil,'user':request.user})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password_confirmation=request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request,'./login/registrar',{'error':'Password confirmation does not match'})
        
        try:
            user=User.objects.create_user(username=username,password=password)
        except IntegrityError:    
            return render(request,'./login/registrar.html',{'error':'Username is already not match'})


        user.email=request.POST['email']
        user.save()

        usuario=perfil(user=user)
        usuario.save()

        return redirect('login')

    return render(request,'./login/registrar.html')

def acerca(request):
    return render(request,'./producto/acerca.html')

def contacto(request):
    return render(request,'./producto/contacto.html')

