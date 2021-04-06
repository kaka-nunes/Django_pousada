# Django Sistema Pousada

O Sistemas Pousada, trata-se de um sistema onde se cadastra hóspedes , funcionários , quartos e faz check- in , além de mostrar o historico de reservas. Este sistema foi implementado usando a linguagem de programação python, em conjuto com a framework Django, utilizando um padrão MVC. O sistema é fundamental para orgazização dos dados da pousada, pois temos controles de quartos , hóspedes e funcinários mantendo tudo de forma organizada com fácil acesso e uma boa compreensão das suas funções.

Para criação da app django sistema hotelaria iniciamos criando uma pasta com o nome da que referência a aplicação como . utilizando o ambiente virtual para criação do projeto. 

## Criando o ambiente virtual


Criando seu ambiente virtual. Vamos chamá-lo de generic myvenv


```python
 -m venv myvenv
```

Ative o ambiente virtual 


```python
.myvenv\Scripts\activate bat .
```

Instalar o framework Django:


```python
python -m pip install --upgrade
pip install django
```



## Criando o projeto Django Sistema hotelaria


```python
django-admin startproject hotel .
```


### Mudando as configurações

fazendo alterações algumas em hotel/settings.py. 


```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```


# Criando uma aplicação


```python
python manage.py startapp pousada
```

Depois de criar uma aplicação, também precisamos dizer ao Django que ele deve usar a aplicação. Fazemos isso no arquivo core/settings.py -- abra-o no seu editor de código. Precisamos encontrar o INSTALLED_APPS e adicionar uma linha com 'pousada', logo acima do ].


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pousada',
]
```

###Criando models para a pousada

No arquivo pousada/models.py
define-se todos os objetos, os relacionamentos feitos entre suas classes. 
Nos relacionamentos feitos temos relacionamento de 1 para muitos (foreignKey).
Código: 

```python
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
#   ('cozinheiro', 'cozinheiro'),
    #('arrumacao, arrumacao'),
    #('recepcao', 'recepcao'),
    ('camareira', 'camareira'),
    ('recepcionista', 'recepcionista')


    

]
ATIVO_CHOICES = [
    ('sim', 'sim'),
    ('não', 'não')
    

]

# Create your models here.
class Hospede(models.Model):
  
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True, null=True, blank=True)
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
        return self.nome_cliente

class Funcionario(models.Model):
   
    nome_funcionario = models.CharField(max_length=150)
    cpf_funcionario = models.CharField(max_length=11)
    telefone_funcionario = models.CharField(max_length=11)
    email_funcionario = models.EmailField(unique=True, null=True, blank=True)
    sexo_funcionario = models.CharField(choices=SEXO2_CHOICES, max_length=20)
    turno = models.CharField(max_length=15)
    cargo =  models.CharField(choices=CARGO_CHOICES, default="", editable=True, max_length=20)
    ativo = models.CharField(choices=ATIVO_CHOICES, max_length=20)
   
    
    def __str__(self):
        return self.nome_funcionario
```


### Criando tabelas no banco de dados

Depois de criar os models , criamos as tabelas no banco.


```python
python manage.py makemigrations pousada
```

```python
python manage.py migrate pousada
```

## Django Admin

No django admin acrescenta-se o código abaixo, para que seja possivel fazer algumas operações como Cadastrar, listar, editar e apagar.

```python
from django.contrib import admin
from .models import Hospede, Quarto, Reserva, Funcionario

admin.site.register(Hospede)
admin.site.register(Quarto)
admin.site.register(Reserva)
admin.site.register(Funcionario)
```


criando um super usuário pois é necessario para fazer o login e controlar o sistema:

```python
python manage.py createsuperuser
```
```python
http://127.0.0.1:8000/admin/
```

## URLs 

Para fazer da http://127.0.0.1:8000/  nossa página principal , é necessário importa as URLs da aplicação pousda para o arquivo pousada/urls.py onde o django irá redirecionar tudo que entra em   http://127.0.0.1:8000/ e procurar por novos caminhos lá :



```python
"""core URL Configuration

[...]
"""
rom django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pousada.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
```

A URL do admin:

```python
path('admin/', admin.site.urls),
```

## views (pousada) 
Na views encontramos todas nossas Query set, que buscam, editam, deletam e cadastram.

```python
from django.shortcuts import render, get_object_or_404, redirect 
from pousada.models import Funcionario , Quarto , Hospede , Reserva
from pousada.forms import QuartoForm, HospedeForm, FuncionarioForm, ReservaForm
import imghdr
# Create your views here.

def deletar_quarto(request, id):
    quarto = get_object_or_404(Quarto, pk=id)
    quarto.delete()
    return render(request, 'pousada/listar_quarto.html', {'quarto':quarto})

def buscar_quarto(request):
    infor = request.POST['infor']
    quartos = Quarto.objects.filter(descricao__contains=infor)
    return render(request, 'pousada/listar_quarto.html',{'quartos': quartos})


def editar_quarto(request, id):
    quarto = get_object_or_404(Quarto, pk=id)
    if request.method == "POST":
        form = QuartoForm(request.POST , request.FILES, instance=quarto)
        if form.is_valid():
            quarto = form.save(commit=False)
            form.save()
            return redirect('detalhar_quarto', id=quarto.id)
    else:
        form = QuartoForm(instance=quarto)
    return render(request, 'pousada/editar_quarto.html', {'form': form})


def cadastrar_quarto(request):
    if request.method == "POST":
        form = QuartoForm(request.POST , request.FILES)
        if form.is_valid():
            quarto = form.save(commit=False)
            img = request.FILES
            dados_img = imghdr.what(img['imagem'])
            if dados_img == 'png' or dados_img == 'jpeg':
                form.save()
            return redirect('detalhar_quarto', id=quarto.id)
    else:
        form = QuartoForm()
    return render(request, 'pousada/editar_quarto.html', {'form': form})

def detalhar_quarto(request, id):
    quarto = get_object_or_404(Quarto, pk=id)
    return render(request, 'pousada/detalhar_quarto.html', {'quarto': quarto}) 

def listar_quarto(request):
    quartos = Quarto.objects.all()
    return render(request, 'pousada/listar_quarto.html', {'quartos': quartos})

def deletar_hospede(request, id):
    hospede = get_object_or_404(Hospede, pk=id)
    hospede.delete()
    return render(request, 'pousada/listar_hospede.html', {'hospede':hospede})


def buscar_hospede(request):
    infor = request.POST['infor']
    hospedes = hospede.objects.filter(nome__contains=infor)
    return render(request, 'pousada/listar_hospede.html',{'hospedes': hospedes})


def editar_hospede(request, id):
    hospede = get_object_or_404(Hospede, pk=id)
    if request.method == "POST":
        form = HospedeForm(request.POST , request.FILES, instance=hospede)
        if form.is_valid():
            hospede = form.save(commit=False)
            form.save()
            return redirect('detalhar_hospede', id=hospede.id)
    else:
        form = HospedeForm(instance=hospede)
    return render(request, 'pousada/editar_hospede.html', {'form': form})


def cadastrar_hospede(request):
    if request.method == "POST":
        form = HospedeForm(request.POST , request.FILES)
        if form.is_valid():
            hospede = form.save(commit=False)
            form.save()
            return redirect('detalhar_hospede', id=hospede.id)
    else:
        form = HospedeForm()
    return render(request, 'pousada/editar_hospede.html', {'form': form})

def detalhar_hospede(request, id):
    hospede = get_object_or_404(Hospede, pk=id)
    return render(request, 'pousada/detalhar_hospede.html', {'hospede': hospede}) 

def listar_hospede(request):
    hospedes = Hospede.objects.all()
    return render(request, 'pousada/listar_hospede.html', {'hospedes': hospedes})


def deletar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()
    return render(request, 'pousada/listar_funcionario.html', {'funcionario': funcionario})

def buscar_funcionario(request):
    infor = request.POST['infor']
    funcionario = funcionario.objects.filter(nome__contains=infor)
    return render(request, 'pousada/listar_funcionario.html',{'funcionario': funcionario})

def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    if request.method == "POST":
        form = FuncionarioForm(request.POST , request.FILES, instance=funcionario)
        if form.is_valid():
            funcionario = form.save(commit=False)
            form.save()
            return redirect('detalhar_funcionario', id=funcionario.id)
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'pousada/editar_funcionario.html', {'form': form})

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST , request.FILES)
        if form.is_valid():
            funcionario = form.save(commit=False)
            form.save()
            return redirect('detalhar_funcionario', id=funcionario.id)
    else:
        form = FuncionarioForm()
    return render(request, 'pousada/editar_funcionario.html', {'form': form})


def detalhar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    return render(request, 'pousada/detalhar_funcionario.html', {'funcionario': funcionario}) 


def listar_funcionario(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'pousada/listar_funcionario.html', {'funcionarios': funcionarios})

def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    return render(request, 'pousada/listar_reserva.html', {'reserva': reserva})

def buscar_reserva(request):
    infor = request.POST['infor']
    reserva = reserva.objects.filter(nome_cliente__contains=infor)
    return render(request, 'pousada/listar_reserva.html',{'reserva': reserva})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    if request.method == "POST":
        form = ReservaForm(request.POST , request.FILES, instance=reserva)
        if form.is_valid():
            reserva = form.save(commit=False)
            form.save()
            return redirect('detalhar_reserva', id=reserva.id)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'pousada/editar_reserva.html', {'form': form})

def cadastrar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST , request.FILES)
        if form.is_valid():
            reserva = form.save(commit=False)
            form.save()
            return redirect('detalhar_reserva', id=reserva.id)
           
    else:
        form = ReservaForm()
    return render(request, 'pousada/editar_reserva.html', {'form': form})

def detalhar_reserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    return render(request, 'pousada/detalhar_reserva.html', {'reserva': reserva})

def listar_reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'pousada/listar_reserva.html', {'reservas': reservas})

```


### Url pousada  (pousada/urls.py)

Todas a urls necessária para acessar nossas funções, e rotas do nosso sistema. 
```python
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.listar_quarto, name='listar_quarto'),
    path('listar_hospede', views.listar_hospede, name='listar_hospede'),
    path('listar_reserva', views.listar_reserva, name='listar_reserva'),
    path('listar_funcionario', views.listar_funcionario, name='listar_funcionario'),
    path('quarto/<int:id>/', views.detalhar_quarto , name='detalhar_quarto'),
    path('quarto/new/', views.cadastrar_quarto, name='cadastrar_quarto'),
    path('quarto/editar/<int:id>/', views.editar_quarto, name='editar_quarto'),
    path('buscar_quarto', views.buscar_quarto, name='buscar_quarto'),
    path('quarto/deletar/<int:id>/', views.deletar_quarto, name='deletar_quarto'),

    path('hospede/<int:id>/', views.detalhar_hospede , name='detalhar_hospede'),
    path('hospede/new/', views.cadastrar_hospede, name='cadastrar_hospede'),
    path('hospede/editar/<int:id>/', views.editar_hospede, name='editar_hospede'),
    path('buscar_hospede', views.buscar_hospede, name='buscar_hospede'),
    path('hospede/deletar/<int:id>/', views.deletar_hospede, name='deletar_hospede'),

    path('funcionario/<int:id>/', views.detalhar_funcionario , name='detalhar_funcionario'),
    path('funcionario/new/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionario/editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('buscar_funcionario', views.buscar_funcionario, name='buscar_funcionario'),
    path('funcionario/deletar/<int:id>/', views.deletar_funcionario, name='deletar_funcionario'),

    path('reserva/<int:id>/', views.detalhar_reserva , name='detalhar_reserva'),
    path('reserva/new', views.cadastrar_reserva, name='cadastrar_reserva'),
    path('reserva/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('buscar_reserva', views.buscar_reserva, name='buscar_reserva'),
    path('reserva/deletar/<int:id>/', views.deletar_reserva, name='deletar_reserva'),
    
    
] 
```



#criando templates da nossa pousada
Nas nossas templates temos diferentes classes como o modelo quarto, hóspede, funcionário e reserva que já foram definidas em models.py e essas templates pode se conectar aos models por meio das views.py.
Exemplo:
No arquivo template/pousada/listar_quarto.html temos o seguinte codigo:
também fazemos uso da restrição para salvar apenas imagens do quarto no formato .png e .jpeg. Para isso vamos utilizar a biblioteca imgdr que ficará responsável por pegar o formato da imagem. 

```python
{% extends 'pousada/base.html' %} 

{% block content %}

    
  <h3 style="color: #f7861c">Quartos </h3>
  <table class="table table-#fca95b table-borderless" style="color: #f3b67e">

    {% for quarto in quartos %}
      <tr>
        <td>
          <a href="{% url 'detalhar_quarto' id=quarto.id %}">
            <!--<img width="200" height="100" src="{{quarto.imagem.url}}"> <br/>-->
            {% if quarto.imagem %}
              <img width="300" height="150" src="{{ quarto.imagem.url }}"></a></br>          
            {% endif %}
          </a>
          Quarto:  {{quarto.numero_quarto}}<br/>
          Status : {{quarto.status_quarto}}<br/>
          Descricao: {{quarto.descricao}}<br/>
          <br/>
        </td>
       
        <td>
          <a class="btn btn-default" href="{% url 'editar_quarto' id=quarto.id %}">
            <button type="button" class="btn btn-outline-warning"> Editar</button>
          </a>
        </td>
        <td>
          <a class="btn btn-default" href="{% url 'deletar_quarto' id=quarto.id %}">
             <button type="button" class="btn btn-outline-warning">Deletar</button>
         </a>
        </td>
      </tr>
      </br> 
    {% endfor %}
  </table>
  <a class="btn btn-default" href="{% url 'cadastrar_quarto' %}">
    <button type="button" class="btn btn-outline-warning">Cadastrar</button>
  </a>
{% endblock %}

```
No arquivo template/pousada/editar_quarto.html, edita os dados do quarto caso seja necessário uma alteração.

```python
{% extends 'pousada/base.html' %}

{% block content %}
    <h2>Quarto</h2>
    <form method="POST" class="table" enctype="multipart/form-data">
    {% csrf_token %}
        <div class="form-group">
            {{ form.as_p}}
        </div>
        </br>
        <button type="submit" class="btn btn-outline-warning" >Salvar</button>
    </form>
{% endblock %}
```
No arquivo template/pousada/detalhar_quarto.html , detalhamos as informações dos quartos.
```python
{% extends 'pousada/base.html' %}
{% block content %}
    {% if quarto.imagem %}
        <img width="300" height="150" src="{{ quarto.imagem.url }}"></a></br>  
        Quarto:  {{quarto.numero_quarto}}<br/>        
    {% endif %}
    
    Status : {{quarto.status_quarto}}<br/>
    Descricao: {{quarto.descricao}}<br/>
    <br/>
    
    
{% endblock %}
```


#Tamplate da página principal base.html

Na base.html temos o codigo base que prepara, organiza e embeleza nossa página inicial listar_quartos.html e tambem links para acessarmos caminhos para outras páginas da nossa aplicação.


```python
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.80.0">
    <title>Pousada Sol Nascente</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/navbar-fixed/">

     

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" >
    <link rel="stylesheet" href="{% static 'navbar-top-fixed.css' %}" >

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>

    
    <!-- Custom styles for this template -->
    
    </head>
    <body style="color: #f7861c" >
    <nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="#"><span style="color:black">POUSADA </span><span style="color: #f7861c">SOL NASCENTE</span></a>
          <ul class="nav navbar-top-links navbar-right">
          </ul>
        </div>
      </div><!-- /.container-fluid -->
      </nav>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'listar_quarto' %}" style="color: #f7861c">Home</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav me-auto mb-2 mb-md-0">
            <!--<li class="nav-item">
              <a class="nav-link active" aria-current="page" href="{% url 'listar_quarto' %}" style="color: #f7861c">Quarto</a>
            </li>-->
            <li class="nav-item">
              <a class="nav-link" href="{% url 'listar_hospede' %}" style="color: #f7861c">Hospede</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'listar_funcionario' %}" style="color: #f7861c">Funcionario</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'listar_reserva' %}" style="color: #f7861c">Reserva</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'cadastrar_reserva' %}" style="color: #f7861c">Check-in</a>
            </li>
          </ul>
          <form class="d-flex" action="{% url 'buscar_quarto' %}" method="POST">
            {% csrf_token %}
              <input name="infor" class="form-control me-2" type="search" placeholder="Pesquisa" aria-label="">
              <button class="btn btn-outline-success" type="submit" style="color: #f7861c">Pesquisar</button>
          </form>
          
        </div>
      </div>
    </nav>
    
  
    <main class="container">
      <img alt="Sol Nascente"  width="400" height="300" src="{{ pousada.logo.url }}"  ><br/>
        <div class="bg-light p-4 rounded" style="color: #e69d5a" >
            
            <br/>
            {% block content %}

            {% endblock %}
        


        </div>
        <div class="row">
            
          <div class="col-sm-12">
            <p class="back-link" align="center" ><span style="color:black">Desenvolvido por  </span> <span style="color: #f7861c">Karine Nunes  </span> - <a href="https://www.ifpi.edu.br/" target="blank" style="color: #f7861c">IFPI</a></p>
          </div>
        </div>
    </main>
    
        <script rel="stylesheet" src="{% static 'js/bootstrap.bundle.min.js'  %}"></script>

    
    </body>
</html>

Na nossa template base utilizou-se também o Bootstrap uma estrutura para criar sites responsivos, e onde podemos encontrar templates prontas.
```

##`Preparando nossos Formulários

 Formulários para adicionar e editar os dados casdastrados no nosso sistema. No django pode-se criar formulários do zero ou optar por um formulário pronto do django, na aplicação pousada optou-se por criar formulários do zero. 

pousada/forms.py

```python
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
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
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
            'email_funcionario': forms.EmailInput(attrs={'class': 'form-control'}),
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

```



## Login , logout e autenticar_usuario do Sistema Hotelaria

Criando  login ,logout na views.py

```python
from django.shortcuts import render, get_object_or_404, redirect 
from pousada.models import Funcionario , Quarto , Hospede , Reserva
from pousada.forms import QuartoForm, HospedeForm, FuncionarioForm, ReservaForm
from django.contrib.auth import  login, logout
import imghdr

def logout_usuario(request):
    logout(request)
    return render(request, 'pousada/login.html',{})


def page_login(request):
    return render(request, 'pousada/login.html', {})
```
Template do login : Formulario login template/pousada/login.html

```python
{% extends 'pousada/base.html' %}
{% block content %}

    <form action="{% url 'autenticar_usuario' %}" method="post">
    {% csrf_token %}
        <form class="row g-3">
            <div class="col-auto">
                <label for="exampleInputEmail" class="form-label">Username</label>
                <input name="username" type="text" class="form-control" id="exampleInputEmail" aria-describedby="emailHelp" >
            </div>
            <div class="col-auto">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input name="password" type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div></br>
            <div class="col-auto">
                <button type="submit" class="btn btn-outline-warning mb-3">Login</button>
                
                
            </div>
            
            
        </form>
    </form>
{% endblock %}
```

##Criando autenticar_usuario do Sistema Hotelaria

criando o autenticar usuário na views.py

```python
from django.shortcuts import render, get_object_or_404, redirect 
from pousada.models import Funcionario , Quarto , Hospede , Reserva
from pousada.forms import QuartoForm, HospedeForm, FuncionarioForm, ReservaForm
from django.contrib.auth import authenticate, login, logout
import imghdr

def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        quartos = Quarto.objects.all()
        return render(request, 'pousada/listar_quarto.html', {'quartos': quartos})
    else:
        return render(request, 'pousada/login.html', {})

```
##Criando autenticar_usuario do Sistema Hotelaria

criando novas urls para login , logout e autenticar usuário na pousada/urls.py

```python
from django.urls import path
from . import views

    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),

```

##Adicionando login e logout na nossa página principal

inserindo novos liks para fazer o login na nossa página principal.

```python
    
        <ul class="nav justify-content-end">
            <li class="nav-item">
              {% if user.is_authenticated %}
                <a class="nav-link activa" aria-current='page' href="{% url 'logout_usuario' %}" style="color: #f7861c"> Sair</a>
              {% else %}
                <a class="nav-link activa" aria-current='page' href="{% url 'page_login' %}" style="color: #f7861c"> Login</a>
              {% endif %}
            </li>
        </ul>

```


### Inserindo segurança na nossa lista de quarto

Vamos adicionar  no arquivo `pousada/templates/pousada/listar_quarto`. Vamos colocar `if user.is_authenticated` que verificará se o usuário está  autenticado em uma sessão no navegador. Trazendo assim segurança ao nosso sitema. 

```python
{% extends 'pousada/base.html' %} 

{% block content %}

  {% if user.is_authenticated %}
    <h3 style="color: #f7861c">Usuário(a):  {{user.username}}</h3>
    <a href="{% url 'logout_usuario' %}" style="color: #f7861c"></a>
  {% else %}
    <p style="color: #f7861c">Você precisa realizar o login.</p>
  {% endif %}
  </br>
  <h3 style="color: #f7861c">Quartos </h3>
  <table class="table table-#fca95b table-borderless" style="color: #f3b67e">

    {% for quarto in quartos %}
      <tr>
        <td>
          <a href="{% url 'detalhar_quarto' id=quarto.id %}">
            <!--<img width="200" height="100" src="{{quarto.imagem.url}}"> <br/>-->
            {% if quarto.imagem %}
              <img width="300" height="150" src="{{ quarto.imagem.url }}"></a></br>          
            {% endif %}
          </a>
          Quarto:  {{quarto.numero_quarto}}<br/>
          Status : {{quarto.status_quarto}}<br/>
          Descricao: {{quarto.descricao}}<br/>
          <br/>
        </td>
        {% if user.is_authenticated %}
        <td>
          <a class="btn btn-default" href="{% url 'editar_quarto' id=quarto.id %}">
            <button type="button" class="btn btn-outline-warning"> Editar</button>
          </a>
        </td>
        <td>
          <a class="btn btn-default" href="{% url 'deletar_quarto' id=quarto.id %}">
             <button type="button" class="btn btn-outline-warning">Deletar</button>
         </a>
        </td>
        {% endif %}
      </tr>
      </br> 
    {% endfor %}
  {% if user.is_authenticated %}
  </table>
  <a class="btn btn-default" href="{% url 'cadastrar_quarto' %}">
    <button type="button" class="btn btn-outline-warning">Cadastrar</button>
  </a>
  {% endif %}
{% endblock %}

```
