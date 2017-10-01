from django.forms import ModelForm
from datetime import datetime
from gpo.diaria.models import ProcessoDeDiaria


class DiariaAddForm(ModelForm):

    def gera_numero(tipo):
        now = datetime.now()
        cont = ProcessoDeDiaria.objects.count()
        if tipo == "processo":
            numero = '{cont}-14/{ano}'.format(cont, ano=now.year)
        elif tipo == "memorando":
            numero = 'MEM{cont}/{ano}'.format(cont, ano=now.year)
        return numero

    ProcessoDeDiaria.numero_processo.default = gera_numero("processo")
    ProcessoDeDiaria.numero_memorando.default = gera_numero("memorando")

    class Meta:
        model = ProcessoDeDiaria
        fields = ['credor', 'destino', 'descricao', 'data_saida', 'data_volta']
