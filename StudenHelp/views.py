from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .forms import EvenClub
from django.contrib.auth import login, authenticate
from django.contrib import messages
def index(request):
    return HttpResponse("run application")
@login_required
def home(request):
    return render(request,'home.html')
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
    return redirect('index') 
def choix(request) :
    return render(request,'choix.html')  
def eventClub(request):
    form = EvenClub()
    context = {'form': form}
    return render(request,'eventClub.html',context)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:

                pass
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})   