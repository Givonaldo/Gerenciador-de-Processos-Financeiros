from django.db import models

class Credor(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(verbose_name=u'Nome', max_length=100, help_text="Nome do Credor", default='None')
    codigo_credor = models.CharField(verbose_name=u'Código do Credor', max_length=100, default='None', help_text="Código do Credor do SIAF")
    telefone = models.CharField(verbose_name=u'Telefone', max_length=100, help_text="Telefone do Credor", default='None')
    email = models.EmailField(max_length=100, default='None')
    endereco = models.CharField(verbose_name=u'Endereço', max_length=100, help_text="Endereço do Credor", default='None')

    def __str__(self):
        return self.nome

class CredorServidor(Credor):
    matricula = models.CharField(verbose_name=u'Matrícula', max_length=10, help_text="Matrícula", default='None')
    funcacao = models.CharField(verbose_name=u'Função', max_length=100, help_text="Função", default='None')
    cpf = models.CharField(verbose_name=u'CPF', max_length=100, help_text="CPF", default='None')

    class Meta:
        verbose_name = 'Credor'
        verbose_name_plural = 'Credores'


class CredorFornecedor(Credor):
    cnpj = models.CharField(verbose_name=u'CNPJ', max_length=100, help_text="CNPJ", default='None')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

