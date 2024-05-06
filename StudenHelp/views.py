from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .forms import EvenClub
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Poste
from .forms import EvenClub , EventSocial ,Stage ,Logement ,Transport ,Recommandation , Poste
from django.views.generic import ListView , CreateView , DetailView
from django.urls import reverse_lazy
def index(request):
    return HttpResponse("run application")
def profile(request) :
    return render( request ,'profile.html')  
@login_required
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, f'Coucou {user.username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
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
def transport(request):
    form = Transport()
    context = {'form': form}
    return render(request, 'transport.html', context)


def recommandation(request):
    form = Recommandation()
    context = {'form': form}
    return render(request, 'recommandation.html', context)
def eventSocial(request):
    form = EventSocial()
    context = {'form': form}
    return render(request, 'eventSocial.html', context)
def stage(request):
    form = Stage()
    context = {'form': form}
    return render(request, 'Stage.html', context)
def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
def logement(request):
    form = Logement()
    context = {'form': form}
    return render(request, 'logement.html', context)

 