from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime
from django.template import loader
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "username already taken.")
            return redirect('/signup/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully.")
        return redirect('/signup/')
    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/login_page/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid password.")
            return redirect('/login_page/')
        else:
            login(request, user)
            return redirect('/recipi/')

    return render(request, 'login.html')


def email(request):
    return render(request, 'email.html')

@login_required(login_url='/login_page/')
def recipi(request):
    if request.method == "POST":
        data = request.POST
        recipi_name = data.get('recipi_name')
        recipi_description = data.get('recipi_description')
        recipi_image = request.FILES.get('recipi_image')


        Recipi.objects.create(
        recipi_name = recipi_name,
        recipi_description = recipi_description,
        recipi_image = recipi_image,
        )
        return redirect('/recipi/')
    queryset = Recipi.objects.all()

    if request.GET.get('search'):
        search_term = request.GET.get('search')
        queryset = queryset.filter(recipi_name__icontains=search_term)  # Fixed the filter syntax


    context = {'recipies':queryset}   
    return render(request, 'recipi.html',context)
    
def logout_page(request):
    logout(request)
    return redirect('/login_page/')

def update_recipi(request, id):
    queryset = get_object_or_404(Recipi, id=id)

    if request.method == 'POST':
        recipi_name = request.POST.get('recipi_name')
        recipi_description = request.POST.get('recipi_description')
        recipi_image = request.FILES.get('recipi_image')

        queryset.recipi_name = recipi_name
        queryset.recipi_description = recipi_description
        
        if recipi_image:
            queryset.recipi_image = recipi_image
        
        queryset.save()
        return redirect('/recipi.html/') 

    context = {'recipe': queryset}
    return render(request, 'update_recipi.html', context)


def delete_recipi(request, id):
    queryset = Recipi.objects.get(id=id)
    queryset.delete()
    return redirect('/recipi/')

