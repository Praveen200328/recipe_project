from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@ login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":


        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get("receipe_description")
        receipe_image=request.FILES.get('receipe_image')

        receipy.objects.create(
            receipe_name=receipe_name,
            
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('/receipes/')
    queryset=receipy.objects.all()
    

    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains = request.GET.get('search'))
    context={'receipes':queryset}
    return render(request,'receipes.html',context)
@ login_required(login_url="/login/")
def delete_receipe(request,id):
    queryset=receipy.objects.get(id=id)

    queryset.delete()

    return redirect('/receipes/')
@ login_required(login_url="/login/")
def update_receipe(request,id):
    queryset=receipy.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get("receipe_description")
        receipe_image=request.FILES.get('receipe_image')
        
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipes/')

    context={'receipe':queryset}
    return render(request,'update_receipe.html',context)
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        Password=request.POST.get('Password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect('/')
        user=authenticate(username=username,password=Password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/')
        else:
            login(request,user)
            return redirect('/receipes/')


    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        Password=request.POST.get('Password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "username already taken")
            return redirect('/register/')
        


        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(Password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/register/')

    return render(request,'register.html')
