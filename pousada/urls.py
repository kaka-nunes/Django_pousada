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
    
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
] 