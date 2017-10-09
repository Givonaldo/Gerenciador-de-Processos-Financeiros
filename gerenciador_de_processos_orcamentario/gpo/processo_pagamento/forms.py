from gpo.processo_pagamento.models import ProcessoPagamento
from django.forms import ModelForm



class ProcessoPagamentoForm(ModelForm):
    class Meta:
        model = ProcessoPagamento
        fields = ['numero_processo', 'numero_memorando', 'natureza_despesa',
                  'credor']
