from django.db import models
from gpo.core.choices import GPOChoices

class ProcessoDeDiaria(models.Model):

    numero_processo = models.CharField(
        verbose_name=u'Número do Processo', max_length=100,
        help_text="Número do Processo", default= '',
        unique=True
    )

    numero_memorando = models.CharField(
        verbose_name=u'Número do Memorando', max_length=100,
        help_text="Número do Memorando", default= '',
        unique=True
    )

    credor = models.ForeignKey('credor.CredorServidor', verbose_name='Credor')
    data_cricacao = models.DateField('Data de Cadastro', auto_now_add=True)
    destino = models.CharField(verbose_name=u'Destino', max_length=100, choices=GPOChoices.MUNICIPIOS_PARAIBA.items())
    descricao = models.TextField('Descrição', blank=True)
    data_saida = models.DateField('Data da Saída',)
    data_volta = models.DateField('Data da Volta',)
    valor = models.CharField(verbose_name=u'Valor', max_length=100, blank=True, default='',
                                      help_text='Valor da Diária')
    numero_empenho = models.CharField(verbose_name=u'NE', max_length=100, blank = True, default = '', help_text='Número da Nota de Empenho')
    nota_empenho = models.FileField(upload_to='empenhoDiaria/%d/%m/%Y/', blank = True, help_text='Nota de Empenho em Formato PDF', max_length=100,)
    numero_liquidacao = models.CharField(verbose_name=u'LD', max_length=100, blank = True, default = '')
    numero_ap = models.CharField(verbose_name=u'AP', max_length=100, blank=True, default='', help_text='Número da Autorização de Pagamento')

    class Meta:
        verbose_name = 'Diária'
        verbose_name_plural = 'Diárias'

