from django.shortcuts import render
from gpo.diaria.forms import DiariaAddForm
from .models import ProcessoDeDiaria
from django.http import Http404

def diaria(request):
    template_name = 'diaria.html'
    return render(request, template_name)

def diaria_add(request):
    if request.method == 'POST':
        form = DiariaAddForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.save()
            pagina_inicial = 'index.html'
            return render(request, pagina_inicial,)
    else:
        form = DiariaAddForm
    return render(request, 'diaria_add.html', {'form': form})

def listagem_diarias(request):
    template_name = 'diarias.html'
    try:
        diarias = ProcessoDeDiaria.objects.all()
        context = {'diarias': diarias}
        return render(request, template_name, context)
    except ProcessoDeDiaria.DoesNotExist:
        raise Http404(u"Diárias Não Existem.")
    return render(request, template_name)

