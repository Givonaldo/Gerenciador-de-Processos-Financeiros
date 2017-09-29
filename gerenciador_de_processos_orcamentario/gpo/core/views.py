from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *


def home(request):
    return render(request, 'core/home.html')

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:home'))
    kwargs['extra_context'] = {'next': reverse('core:home')}
    kwargs['template_name'] = 'core/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('core:home')
    return logout(request, *args, **kwargs)


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('core:login')
    template_name = "core/register.html"

def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)

def sobre(request):
    template_name = 'core/sobre.html'
    return render(request, template_name)

def credor(request):
    template_name = 'credores/credor.html'
    return render(request, template_name)

def credor_servido_add(request):
    if request.method == 'POST':
        form = CredorServidorForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.save()
            return render(request, 'core/index.html',)
    else:
        form = CredorServidorForm()
    return render(request, 'credores/credor_servidor_add.html', {'form': form})

def credorFornecedorAdd(request):
    pass

def diaria(request):
    template_name = 'processos/diaria.html'
    return render(request, template_name)

def diaria_add(request):
    if request.method == 'POST':
        form = DiariaAddForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.save()
            return render(request, 'core/index.html',)
    else:
        form = DiariaAddForm
    return render(request, 'processos/diaria_add.html', {'form': form})

def listagem_diarias(request):
    try:
        diarias_cadastradas = ProcessoDeDiaria.objects.all()
    except ProcessoDeDiaria.DoesNotExist:
        raise Http404(u"Fornecedor não existe.")
    template_name = 'processos/diarias.html'
    return render(request, template_name)