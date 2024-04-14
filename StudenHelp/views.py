from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
def index(request):
    return HttpResponse("Première apllication django")

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') # Remplacez 'home' par le nom de votre URL de page d'accueil
            else:
                error_message = "Identifiants invalides. Veuillez réessayer."
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})
    