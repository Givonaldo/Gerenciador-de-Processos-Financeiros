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

    def save(self, commit=True):
        instance = super(CredorServidor, self).save(commit=False)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = CredorServidor
        fields = ['nome', 'matricula', 'codigo_credor', 'telefone',
                  'email', 'endereco', 'funcacao', 'cpf']
