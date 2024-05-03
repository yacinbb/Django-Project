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


