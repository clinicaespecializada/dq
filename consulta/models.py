from django.db import models
from paciente.models import Paciente
# Create your models here.



class ClinicoPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

class Clinico(models.Model):
    data_atendimento = models.DateField()
    descricao_atendimento = models.TextField()
    paciente = models.ForeignKey(ClinicoPaciente, on_delete=models.PROTECT)


class PsiquiatraPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)


class Psiquiatra(models.Model):
    data_atendimento = models.DateField()
    descricao_atendimento = models.TextField()
    paciente = models.ForeignKey(PsiquiatraPaciente, on_delete=models.PROTECT)

class PsicologoPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

class Psicologo(models.Model):
    data_atendimento = models.DateField()
    descricao_atendimento = models.TextField()
    paciente = models.ForeignKey(PsicologoPaciente, on_delete=models.PROTECT)