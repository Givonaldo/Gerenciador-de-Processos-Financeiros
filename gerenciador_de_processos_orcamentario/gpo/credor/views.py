from django.shortcuts import render

from gpo.credor.forms import CredorServidorForm, CredorFornecedorForm


def credor(request):
    template_name = 'credor.html'
    return render(request, template_name)

def credor_servido_add(request):
    if request.method == 'POST':
        form = CredorServidorForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.save()
            return render(request, 'index.html',)
    else:
        form = CredorServidorForm()
    return render(request, 'credor_servidor_add.html', {'form': form})

def credor_fornecedor_add(request):
    if request.method == 'POST':
        form = CredorFornecedorForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            return render(render, 'index.html')
    else:
        form = CredorFornecedorForm()
    return render(render, 'credor_fornecedor_add.html', {'form': form})

