from django.db import models

class Paciente(models.Model):

    STATUS = (
        ('1','ATIVO'),
        ('2','INATIVO'),
        ('3','TRIAGEM'),
    )

    nome = models.CharField(max_length=155)
    genero = models.CharField(max_length=155)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=155)
    cidade_origem = models.CharField(max_length=155)
    estado_civil = models.CharField(max_length=155)
    escolaridade = models.CharField(max_length=155)
    religiao = models.CharField(max_length=155)
    situacao_profissional = models.CharField(max_length=155)
    profissao = models.CharField(max_length=155)
    filhos = models.BooleanField(default=False)
    status  = models.CharField(max_length=155, choices = STATUS)


    def __str__(self) -> str:
        return self.nome


class EnderecoPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cep = models.CharField(max_length=155)
    pais = models.CharField(max_length=155)
    estado = models.CharField(max_length=155)
    cidade = models.CharField(max_length=155)
    bairro = models.CharField(max_length=155)
    rua = models.CharField(max_length=155)
    numero = models.IntegerField()

    def __str__(self) -> str:
        return self.paciente.nome
    
class Responsavel(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=155)
    telefone = models.CharField(max_length=155)

    def __str__(self) -> str:
        return self.Paciente.nome







# class Internacoes(models.Model):
#     local = models.CharField(max_length=155)
#     tempo = models.CharField(max_length=155)



# class Paciente(models.Model):
#     TEMPO_INTERNACAO = (
#         ('3','Tres meses'),
#         ('6','Seis meses'),
#         ('9','Nove meses'),
#     )
#     GRAU_INSTRUCAO=(
#         ('1','Promeiro gral'),
#         ('2','Segundo gral'),
#         ('3','Terceiro gral')
#     )
#     EXERCICIO = (
#         ('1','Futebol'),
#         ('2','Caminhada'),
#         ('3','Academia'),
#         ('4','Corrida'),
#     )
#     nome_paciente = models.CharField(max_length=155)
#     contato_paciente = models.CharField(max_length=155)
#     idade = models.IntegerField()
#     data_entrada = models.DateField()
#     grau_instrucao = models.CharField(max_length=155, choices=GRAU_INSTRUCAO)
#     profissao = models.CharField(max_length=155)
#     data_nascimento = models.DateField()    
    
#     motivo_internacao = models.CharField(max_length=155)
#     quantidade_internacao = models.IntegerField()
#     tempo_internado = models.IntegerField()
#     endereço_linha_1 = models.CharField(max_length=155)
#     endereço_linha_2 = models.CharField(max_length=155)
#     renda_familiar = models.DecimalField(max_digits=10, decimal_places=2)
#     nome_responsavel_legal = models.CharField(max_length=155)
#     grau_relacionamento= models.CharField(max_length=155)
#     contato_responsavel_legal = models.CharField(max_length=155)
#     praticas_exercicio_fisico = models.CharField(choices=EXERCICIO, max_length=155)
#     praticas_intelectuais = models.TextField()
#     hobbies = models.TextField()
#     habitos_lazer = models.CharField(max_length=155)
#     talentos = models.CharField(max_length=155)
#     tempo_previsto_internacao= models.CharField(choices=TEMPO_INTERNACAO, max_length=155)
#     observacoes = models.TextField()
#     outros_tratamentos = models.TextField()
#     estrutura_familiar = models.TextField()
#     doenças_pre_existentes = models.TextField()
#     alergias = models.CharField(max_length=155)
#     dieta_especial = models.CharField(max_length=155, blank=True, null=True)
#     situacao_judicial = models.CharField(max_length=155)


# # historico

# class Medicacao(models.Model):
#     nome = models.CharField(max_length=155)
#     horario = models.TimeField()
#     paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)