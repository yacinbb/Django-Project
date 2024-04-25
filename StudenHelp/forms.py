from django.forms import ModelForm , CharField ,PasswordInput 
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class LoginForm(ModelForm):
    password = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password'] 
class UserRegistrationForm(UserCreationForm):
    nom = forms.CharField(label='Prénom')
    prenom = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    telephone = forms.CharField(max_length=20)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('nom', 'prenom' , 'email','telephone')        