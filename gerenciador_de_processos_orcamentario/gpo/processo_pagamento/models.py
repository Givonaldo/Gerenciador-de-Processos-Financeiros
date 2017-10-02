from django.db import models
from gpo.core.choices import GPOChoices


class ProcessoPagamento(models.Model):

    numero_processo = models.CharField(
        verbose_name=u'Número do Processo', max_length=100,
        help_text="Número do Processo", default='',
        unique=True
    )

    numero_memorando = models.CharField(
        verbose_name=u'Número do Memorando', max_length=100,
        help_text="Número do Memorando", default='',
        unique=True
    )

    natureza_despesa = models.CharField(verbose_name=u'Natureza da Despesa', max_length=100,
                                        choices=GPOChoices.NATUREZA_DA_DESPESA.items())

    credor = models.ForeignKey('credor.CredorFornecedor', verbose_name='Credor')
    valor_bruto = models.CharField(verbose_name=u'Valor', max_length=100, blank=True, default='',
                                      help_text='Valor Bruto')
    data_cricacao = models.DateField('Data de Cadastro', auto_now_add=True)
    descricao = models.TextField('Descrição', blank=True)
    numero_empenho = models.CharField(verbose_name=u'NE', max_length=100, blank=True, default='',
                                      help_text='Número da Nota de Empenho')
    nota_empenho = models.FileField(upload_to='empenhoProcesso/%d/%m/%Y/', blank=True,
                                    help_text='Nota de Empenho em Formato PDF', max_length=100, )
    numero_liquidacao = models.CharField(verbose_name=u'LD', max_length=100, blank=True, default='')
    numero_ap = models.CharField(verbose_name=u'AP', max_length=100, blank=True, default='',
                                 help_text='Número da Autorização de Pagamento')
    numero_ap_ex = models.CharField(verbose_name=u'AP EX', max_length=100, blank=True, default='',
                                 help_text='Número da Autorização de Pagamento Extra Orçamentária')
    valor_liquido = models.CharField(verbose_name=u'Valor Líquido', max_length=100, blank=True, default='',
                                 help_text='Valor Líquido',)

    class Meta:
        verbose_name = "Processo"
        verbose_name_plural = "Processos"


class TomadaDePreco(models.Model):

    tomada1 = models.ForeignKey('processo_pagamento.ConsultaDePreco')
    tomada2 = models.ForeignKey('processo_pagamento.ConsultaDePreco')
    tomada3 = models.ForeignKey('processo_pagamento.ConsultaDePreco')


class ConsultaDePreco():
    numero_tomada = models.CharField()
    credor = models.ForeignKey('credor.CredorFornecedor', verbose_name='Credor')
    itens = models.ManyToManyField(ItemMaterialDeConsumo)


class OrdemPagamento():
    pass

class ItemDeDespesa():
    pass


class ItemMaterialDeConsumo():
    nome = models.CharField()
    valor_unitario = models.CharField(verbose_name='Valor Unitário', )
    tipo_de_medida = models.CharField(verbose_name='Tipo de Unidade de Medida', max_length=100,
                                        choices=GPOChoices.NATUREZA_DA_DESPESA.items())
    def __str__(self):
        self.nome

class NaturezaDaDespesa():
    codigo = models.CharField(verbose_name='Código Natureza da Despesa', max_length=100)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)

    def __str__(self):
        self.descricao