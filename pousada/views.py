from django.shortcuts import render, get_object_or_404, redirect 
from pousada.models import Funcionario , Quarto , Hospede , Reserva
from pousada.forms import QuartoForm, HospedeForm, FuncionarioForm, ReservaForm
from django.contrib.auth import authenticate, login, logout
import imghdr
# Create your views here.

def logout_usuario(request):
    logout(request)
    return render(request, 'pousada/login.html',{})


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


def page_login(request):
    return render(request, 'pousada/login.html', {})

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
    

