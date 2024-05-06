from django.forms import ModelForm , CharField ,PasswordInput 
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import Poste , Evenement,EvenClub
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Poste , Evenement,tp, ts , EvenClub,EvenSocial , Stage , Logement , Transport , Recommandation
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'login-form'
    helper.form_show_labels = False
    helper.add_input(Submit('submit', 'Se connecter', css_class='btn-primary'))

class UserRegistrationForm(UserCreationForm):
    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(label='Prenom')
    email = forms.EmailField(label='Adresse e-mail')
    telephone = forms.CharField(max_length=20)
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nom', 'prenom' , 'email','telephone') 
class Poste(forms.Form):
    image = forms.ImageField(label='image')
    type = forms.IntegerField(label='type')
    date = forms.DateField(label='date')
    # users = forms.ModelChoiceField(queryset=User.objects.all(), label='users')
    class Meta:
        model = Poste
        fields = ['image' ,'type','date']           
class Evenement(Poste) :
    intitule = forms.CharField(label='intitule')
    description = forms.CharField(label='description')
    lieu = forms.CharField(label='lieu')
    contactinfo = forms.CharField(label='Contact ')
    class Meta() :
        model = Evenement
        fields = "__all__"
class EvenClub(Evenement):
    club = forms.CharField(label='Club')  
    class Meta() :
        model = EvenClub
        fields = "__all__"
class Transport(Poste):
    depart = forms.CharField(label='départ')
    destination = forms.CharField(label='destination')
    # mochkla mayjibech TimeField
    heure_dep = forms.TimeField(label='heure de destination ')
    nbre_sieges = forms.IntegerField(label='nbre siége')
    contactinfo = forms.CharField(label='contactinfo')
    class Meta():
        model = Transport
        fields = "__all__"
class Recommandation(Poste):
    text = forms.CharField(label='text')
    class Meta():
        model = Recommandation
        fields = "__all__"
class EventSocial(Evenement):
    prix = forms.CharField(label='prix')
    class Meta():
        model = EvenSocial
        fields = "__all__"
class Stage(Poste):
    specialite = forms.CharField(label='spécialité ')
    typestg = forms.ChoiceField(choices=ts, label='type de stage')
    Societe = forms.CharField(label='société')
    sujet = forms.CharField(label='sujet')
    contactinfo = forms.CharField(label='Contact ')
    duree = forms.IntegerField(label='durée')
    class Meta():
        model = Stage
        fields = "__all__"   
class Logement(Poste):
    localisation = forms.CharField(label='localisation')
    description = forms.CharField(label='description')
    contactinfo = forms.CharField(label='contactinfo')
    class Meta():
        model = Logement
        fields = "__all__"        
