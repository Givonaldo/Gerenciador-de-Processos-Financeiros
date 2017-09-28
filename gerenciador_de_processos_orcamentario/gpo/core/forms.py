from django.contrib.auth.forms import *
from django.forms import forms
from django.forms import ModelForm
from .models import MyUser, ProcessoDeDiaria
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'email']

class DiariaAddForm(ModelForm):
    class Meta:
        model = ProcessoDeDiaria
        fields = ['credor', 'destino', 'descricao', 'data_saida', 'data_volta']