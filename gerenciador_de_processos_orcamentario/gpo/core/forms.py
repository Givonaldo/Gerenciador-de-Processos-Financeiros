from django.contrib.auth.forms import *
from django.forms import forms
from django.forms import ModelForm
from .models import MyUser, ProcessoDeDiaria, CredorServidor
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'email']

class DiariaAddForm(ModelForm):
    class Meta:
        model = ProcessoDeDiaria
        fields = ['credor', 'destino', 'descricao', 'data_saida', 'data_volta']


class CredorServidorForm(ModelForm):
    class Meta:
        model = CredorServidor
        fields = ['nome', 'matricula', 'codigo_credor', 'funcacao', 'cpf',
                  'endereco', 'telefone', 'email']
