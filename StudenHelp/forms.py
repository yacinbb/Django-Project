from django.forms import ModelForm , CharField ,PasswordInput 
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import Poste , Evenement,EvenClub
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Se connecter'))
class UserRegistrationForm(UserCreationForm):
    nom = forms.CharField(label='Prénom')
    prenom = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    telephone = forms.CharField(max_length=20)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nom', 'prenom' , 'email','telephone') 
class Poste(forms.Form):
    class Meta:
        model = Poste
        fields = "all"           
class Evenement(Poste) :
    intitule = forms.CharField(label='intitule')
    description = forms.CharField(label='decription')
    lieu = forms.CharField(label='lieu')
    contactinfo = forms.CharField(label='Contact ')
    class Meta() :
        model = Evenement
        fields = "__all__"
class EvenClub(Evenement):
    class Meta() :
        model = EvenClub
        fields = "__all__"


