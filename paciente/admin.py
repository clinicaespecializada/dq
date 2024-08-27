from django.contrib import admin
from .models import Paciente, EnderecoPaciente,Responsavel



@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['id','nome']

    
@admin.register(EnderecoPaciente)
class EnderecoPacienteAdmin(admin.ModelAdmin):
    list_display = ['id','paciente']

@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ['id','paciente']