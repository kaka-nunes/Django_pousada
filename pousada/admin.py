from django.contrib import admin
from .models import Hospede, Quarto, Reserva, Funcionario

admin.site.register(Hospede)
admin.site.register(Quarto)
admin.site.register(Reserva)
admin.site.register(Funcionario)

# Register your models here.
