from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(label='Aluno', max_length=100)
    idade = forms.IntegerField(label='Idade')
    responsavel = forms.CharField(label='Nome Responsável', max_length=100)
    email = forms.EmailField(label='Email Responsável')
    telefone = forms.CharField(label='Telefone', max_length=20)