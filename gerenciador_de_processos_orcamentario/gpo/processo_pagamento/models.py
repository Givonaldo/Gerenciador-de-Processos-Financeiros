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


class MapaComparativo(models.Model):

    tomada1 = models.OneToOneField('processo_pagamento.ConsultaDePreco', verbose_name='Tomada 1', blank=True, default='', related_name="tomada_de_preco1")
    tomada2 = models.OneToOneField('processo_pagamento.ConsultaDePreco', verbose_name='Tomada 2', blank=True, default='' ,related_name="tomada_de_preco2")
    tomada3 = models.OneToOneField('processo_pagamento.ConsultaDePreco', verbose_name='Tomada 3', blank=True, default='', related_name="tomada_de_preco3")

    menor_preco = models.CharField(verbose_name='Menor Preço: ', max_length=100, blank=True, default='')
    preco_medio = models.CharField(verbose_name='Preço Médio:', max_length=100, blank=True, default='')

    ganhador = models.ForeignKey('credor.CredorFornecedor', verbose_name='Credor')


class ConsultaDePreco(models.Model):
    numero_tomada = models.CharField(
        verbose_name=u'Número da Consulta', max_length=100,
        help_text="Número da Consulta de Preço", default='',
        unique=True
    )
    credor = models.ForeignKey('credor.CredorFornecedor', verbose_name='Credor')
    itens = models.ManyToManyField('processo_pagamento.ItemMaterialDeConsumo')

    def __str__(self):
        self.numero_tomada

class OrdemPagamento(models.Model):
    numero_ordem = models.CharField(
        verbose_name=u'Número da Ordem', max_length=100,
        help_text="Número da Ordem de Preço", default='',
        unique=True
    )
    consulta_vencedora = models.ForeignKey('processo_pagamento.MapaComparativo')


class ItemDeDespesa(models.Model):
    pass


class ItemMaterialDeConsumo(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100,)
    valor_unitario = models.CharField(verbose_name='Valor Unitário', max_length=100,)
    tipo_de_medida = models.CharField(verbose_name='Tipo de Unidade de Medida', max_length=100,)
    def __str__(self):
        self.nome

class NaturezaDaDespesa(models.Model):
    codigo = models.CharField(verbose_name='Código Natureza da Despesa', max_length=100)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)

    def __str__(self):
        self.descricao