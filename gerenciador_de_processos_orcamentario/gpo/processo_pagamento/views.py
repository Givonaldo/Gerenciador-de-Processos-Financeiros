from django.shortcuts import render

# Create your views here.
from gpo.processo_pagamento.forms import ProcessoPagamentoForm


def processo_pagamento(request):
    template_name = 'processo_pagamento.html'
    return render(request, template_name)


def criar_processo_pagamento(request):

    if request.method == 'POST':
        form = ProcessoPagamentoForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.save()
            pagina_inicial = 'index.html'
            return render(request, pagina_inicial,)
    else:
        form = ProcessoPagamentoForm
    return render(request, 'processo_pagamento_add.html', {'form': form})
