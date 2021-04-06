import os
import uuid
from django.db import models
from django.conf import settings

SEXO_CHOICES =[
    ('feminino', 'feminino'),
    ('masculino', 'masculino')
    
]
STATUS_QUARTO = [
    ('ocupado', 'ocupado'),
    ('disponivel', 'disponivel')
    
]

CHECKIN_CHOICES=[
    ('checkin', 'checkin'),
    ('checkout', 'checkout')
    
    
]
SEXO2_CHOICES =[
    ('feminino', 'feminino'),
    ('masculino', 'masculino')
]

CARGO_CHOICES = [
    ('camareira', 'camareira'),
    ('recepcionista', 'recepcionista')
    #('cozinheiro', 'cozinheiro'),
    #('arrumacao, arrumacao'),
    #('recepcao', 'recepcao')


    

]
ATIVO_CHOICES = [
    ('sim', 'sim'),
    ('não', 'não')
    

]

# Create your models here.
class Hospede(models.Model):
  
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(unique=True, null=False, blank=False)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=20)

    def __str__(self):
        return str(self.cpf)

class Quarto(models.Model):
    numero_quarto = models.PositiveIntegerField()
    status_quarto = models.CharField(choices=STATUS_QUARTO, max_length=20)
    descricao= models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='pousada/media', blank=True)
    

    def __str__(self):
        return str(self.numero_quarto)
  
   

class Reserva(models.Model):
   
    nome_cliente = models.CharField(default="", editable=True, max_length=100)
    cpf = models.ForeignKey(Hospede, on_delete=models.CASCADE, verbose_name="Cpf Cliente")
    numero_quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, verbose_name="Numero Quarto")
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()
    valor = models.FloatField()
    status_reserva= models.CharField(choices=CHECKIN_CHOICES, max_length=20)


    def __str__(self):
        return str(self.cpf)

class Funcionario(models.Model):
   
    nome_funcionario = models.CharField(max_length=150)
    cpf_funcionario = models.CharField(max_length=14)
    telefone_funcionario = models.CharField(max_length=14)
    email_funcionario = models.EmailField(unique=True, null=False, blank=False)
    sexo_funcionario = models.CharField(choices=SEXO2_CHOICES, max_length=20)
    turno = models.CharField(max_length=15)
    cargo =  models.CharField(choices=CARGO_CHOICES, default="", editable=True, max_length=20)
    ativo = models.CharField(choices=ATIVO_CHOICES, max_length=20)
   
    
    def __str__(self):
        return self.nome_funcionario