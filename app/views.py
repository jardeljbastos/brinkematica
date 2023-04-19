from django.shortcuts import render
from .forms import CadastroForm

def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            responsavel = form.cleaned_data['responsavel']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            return render(request, 'sucesso.html', {'nome': nome})
    return render(request, 'cadastro.html', {'form': form})

# Create your views here.
