from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import EvenClub , Poste
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import  Stage ,Logement ,Transport ,Recommandation
from .forms import EvenClubForms , TransportForm , EvenementForm, RecommandationForm , StageForm ,LogementForm , EventSocialForm

def index(request):
    return HttpResponse("run application")

def profile(request):
    return render(request ,'profile.html')

@login_required
def home(request):
    posts = Poste.objects.all()
    evenement_form = EvenementForm()
    even_club_form = EvenClubForms()
    transport_form =TransportForm()
    recommandation_form = RecommandationForm()
    stage_form = StageForm()
    logement_form = LogementForm()
    return render(request, 'home.html', {
        'posts': posts,
        'evenement_form': evenement_form,
        'even_club_form': even_club_form,
        'transport_form': transport_form,
        'recommandation_form': recommandation_form,
        'stage_form': stage_form,
        'logement_form': logement_form,
    })

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

def choix(request):
    return render(request, 'choix.html')

def eventClub(request):
    if request.method == 'POST':
        form = EvenClubForms(request.POST , request.FILES)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.users_id = request.user.id
            poste.save()
            return redirect('home')
    else:
        form = EvenClubForms()

    return render(request, 'eventClub.html', {'form': form})

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
    if request.method == 'POST':
        form = TransportForm(request.POST , request.FILES)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.users_id = request.user.id
            poste.save()
            return redirect('home')
    else:
        form = TransportForm()

    return render(request, 'transport.html', {'form': form})

def recommandation(request):
    if request.method == 'POST':
        form = RecommandationForm(request.POST , request.FILES)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.users_id = request.user.id
            poste.save()
            return redirect('home')
    else:
        form = RecommandationForm()

    return render(request, 'recommandation.html', {'form': form})
def post(request) :
    form = Poste()
    context = {'form': form}
    return render(request, 'post.html', context)
def eventSocial(request):
    if request.method == 'POST':
        form = EventSocialForm(request.POST , request.FILES)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.users_id = request.user.id
            poste.save()
            return redirect('home')
    else:
        form = EventSocialForm()

    return render(request, 'eventSocial.html', {'form': form})

def stage(request):
    if request.method == 'POST':
        form = StageForm(request.POST , request.FILES)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.users_id = request.user.id
            poste.save()
            return redirect('home')
    else:
        form = StageForm()

    return render(request, 'Stage.html', {'form': form})

def logement(request):
    if request.method == 'POST':
        form = LogementForm(request.POST , request.FILES)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.users_id = request.user.id
            poste.save()
            return redirect('home')
    else:
        form = LogementForm()

    return render(request, 'logement.html', {'form': form})
def evenemnt(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST , request.FILES)
        if form.is_valid():
            poste = form.save(commit=False)
            poste.users_id = request.user.id
            poste.save()
            return redirect('home')
    else:
        form = EvenementForm()

    return render(request, 'logement.html', {'form': form})