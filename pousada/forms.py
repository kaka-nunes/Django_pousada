from django import forms

from pousada.models import Quarto, Hospede , Funcionario, Reserva 


class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ('numero_quarto', 'status_quarto', 'descricao', 'imagem')

        widgets = {
            'numero_quarto': forms.TextInput(attrs={'class': 'form-control'}),
            'status_quarto': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
        }

class HospedeForm(forms.ModelForm):
    class Meta:
        model = Hospede
        fields = ('nome', 'cpf', 'telefone', 'email', 'sexo')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={ 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={ 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome_funcionario', 'cpf_funcionario', 'telefone_funcionario', 'email_funcionario', 'sexo_funcionario', 'turno', 'cargo', 'ativo')

        widgets = {
            'nome_funcionario': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_funcionario': forms.TextInput(attrs={ 'class': 'form-control'}),
            'telefone_funcionario': forms.TextInput(attrs={'class': 'form-control'}),
            'email_funcionario': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo_funcionario': forms.Select(attrs={'class': 'form-control'}),
            'turno': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'ativo': forms.Select(attrs={'class': 'form-control'}),
            
            
        }

class ReservaForm(forms.ModelForm):
    class Meta: 
        model = Reserva
        fields = ('nome_cliente', 'cpf', 'numero_quarto', 'data_entrada', 'data_saida', 'valor')

        widgets = {
            'nome_cliente' : forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.Select(attrs={'class': 'form-control'}),
            'numero_quarto': forms.Select(attrs={'class': 'form-control'}),
            'data_entrada' : forms.DateInput(attrs={'class': 'form-control'}),
            'data_saida' : forms.DateInput(attrs={'class': 'form-control'}),
            'status_reserva': forms.Select(attrs={'class': 'form-control'}),
            'valor' : forms.TextInput(attrs={'class': 'form-control'}),
            

        }
