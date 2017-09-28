from django.core.urlresolvers import reverse

from django.db import models
from gpo import core
from gpo.core.choices import GPOChoices
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Email address'),
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('Nome'),
        max_length=50,
        blank=False,
        help_text=_('Inform your name'),
    )
    last_name = models.CharField(
        verbose_name=_('Sobrenome'),
        max_length=50,
        blank=False,
        help_text=_('Inform your last name'),
    )
    USERNAME_FIELD = 'email'
    objects = EmailUserManager()

class ProcessoDeDiaria(models.Model):
    credor = models.ForeignKey('core.CredorServidor', verbose_name='Credor')
    data_cricacao = models.DateField('Data de Cadastro', auto_now_add=True)
    destino = models.CharField(verbose_name=u'Destino', max_length=100, choices=GPOChoices.MUNICIPIOS_PARAIBA.items())
    descricao = models.TextField('Descrição', blank=True)
    data_saida = models.DateField('Data da Saída',)
    data_volta = models.DateField('Data da Volta',)

    class Meta:
        verbose_name = 'Diária'
        verbose_name_plural = 'Diárias'


class ProcessoDePagamento(models.Model):

    pass


class CredorServidor(models.Model):

    pass


class CredorFornecedor(models.Model):

    pass





