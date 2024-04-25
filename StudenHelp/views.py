from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def index(request):
    return HttpResponse("Première apllication django")

@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return render(request,'home.html',context)
def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})
def logout_view(request):
    logout(request)
    return redirect('acceuil')   