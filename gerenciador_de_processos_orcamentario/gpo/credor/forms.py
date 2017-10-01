from django.contrib.auth.forms import *
from django.forms import ModelForm
from .models import CredorServidor, CredorFornecedor



class CredorServidorForm(ModelForm):
    class Meta:
        model = CredorServidor
        fields = ['nome', 'matricula', 'codigo_credor', 'telefone',
                  'email', 'endereco', 'funcacao', 'cpf']

class CredorFornecedorForm(ModelForm):
    class Meta:
        model = CredorFornecedor
        fields = ['nome', 'codigo_credor', 'telefone', 'email', 'endereco', 'cnpj']