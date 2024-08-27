from django.contrib import admin
from .models import PsicologoPaciente,ClinicoPaciente,PsiquiatraPaciente,Clinico,Psicologo,Psiquiatra


class ClinicoInline(admin.TabularInline):
    model = Clinico
    extra  = 1

@admin.register(ClinicoPaciente)
class ClinicoPaciente(admin.ModelAdmin):
    list_display = ['id','paciente']
    inlines = [ClinicoInline]

class PsicologoInline(admin.TabularInline):
    model = Psicologo
    extra  = 1

@admin.register(PsicologoPaciente)
class PsicologoPaciente(admin.ModelAdmin):
    list_display = ['id','paciente']
    inlines = [PsicologoInline]

class PsiquiatragoInline(admin.TabularInline):
    model = Psiquiatra
    extra  = 1
@admin.register(PsiquiatraPaciente)
class PsiquiatraPaciente(admin.ModelAdmin):
    list_display = ['id','paciente']
    inlines = [PsiquiatragoInline]