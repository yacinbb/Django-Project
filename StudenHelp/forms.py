from django.forms import ModelForm , CharField ,PasswordInput 
from django.contrib.auth.models import User
class LoginForm(ModelForm):
    password = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password'] 