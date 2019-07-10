from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm, DateInput, DateField
import datetime

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('rut', 'fechanac', 'direccion',)

        labels = {
			'rut':'RUT',
			'fechanac':'Fecha de nacimiento',
			'direccion':'Dirección',
            }
        widgets = {
			'fechanac': forms.SelectDateWidget(years=range(datetime.datetime.now().year - 100, datetime.datetime.now().year)),
        }

class SignUpForm(UserCreationForm):
    rut = forms.CharField(max_length=30,label = 'RUT', widget= forms.TextInput(attrs={'class':'form-input','placeholder': 'Ingrese su RUT'}))
    fechanac = forms.DateField(label='Fecha de nacimiento', widget = forms.SelectDateWidget(
        years=range(datetime.datetime.now().year - 100, datetime.datetime.now().year),
        attrs={'placeholder': 'Ingrese su fecha de nacimiento'}))
    direccion = forms.CharField(max_length=30, label='Dirección', widget = forms.TextInput(attrs={'class':'form-input','placeholder': 'Ingrese su dirección'})) 

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','first_name','last_name','email','rut', 'fechanac', 'direccion')
        widgets = {
                'username': forms.TextInput(attrs={'class':'form-input','placeholder': 'Seleccione un nombre de usuario'}),
                'password1': forms.PasswordInput(attrs={'class':'form-input','placeholder': 'Ingrese su contraseña'}),
                'password2': forms.PasswordInput(attrs={'class':'form-input','placeholder': 'Repita su contraseña'}),
                'first_name': forms.TextInput(attrs={'class':'form-input','placeholder': 'Ingrese su nombre'}),
                'last_name': forms.TextInput(attrs={'class':'form-input','placeholder': 'Ingrese sus apellidos'}),
                'email': forms.TextInput(attrs={'class':'form-input','placeholder': 'Ingrese su correo electrónico'}),
                
        }
