from django.forms import ModelForm , CharField ,PasswordInput 
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Poste , Evenement,tp, ts , EvenClub,EvenSocial , Stage , Logement , Transport ,Recommandation

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

class PosteF(forms.Form):
    image = forms.ImageField(label='image')
    type = forms.IntegerField(label='type')
    date = forms.DateField(label='date')
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'
    fields = ['image' , 'type', 'date']
class EvenClubForms(forms.ModelForm):
    class Meta:
        model = EvenClub
        fields = ['intitule', 'description', 'lieu', 'contactinfo', 'club','image','type','date']
class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['intitule', 'description', 'lieu', 'contactinfo']
class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['depart', 'destination', 'heure_dep', 'nbre_sieges', 'contactinfo','image','type','date']
class RecommandationForm(forms.ModelForm):
    class Meta:
        model = Recommandation
        fields = ['text']
class EventSocialForm(forms.ModelForm):
    class Meta:
        model = EvenSocial
        fields = ['prix']
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['specialite','typestg' ,'societe' , 'sujet' , 'contactinfo' ,'duree','image','type','date']
class LogementForm(forms.ModelForm):
    class Meta:
        model = Logement
        fields = ['image' , 'type', 'date' ,'localisation','description' ,'contactinfo']



