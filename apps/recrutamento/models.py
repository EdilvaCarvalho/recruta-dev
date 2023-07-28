from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Endereco(models.Model):
    cep = models.CharField(max_length=9, null=False, blank=False)
    cidade = models.CharField(max_length=70, null=False, blank=False)
    estado = models.CharField(max_length=70, null=False, blank=False)
    rua = models.CharField(max_length=70, null=False, blank=False)
    bairro = models.CharField(max_length=70, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False, verbose_name="Número")
    complemento = models.CharField(max_length=150)

class Candidato(models.Model):
    GENERO = [
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("NB", "Não-binário"),
        ("O", "Masculino"),
        ("PNR", "Prefiro não responder")
    ]

    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(blank=False, null=False, verbose_name="Data de nascimento") 
    genero = models.CharField(max_length=4, choices=GENERO, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    linkedin = models.URLField(max_length=200, verbose_name="LinkedIn")
    github = models.URLField(max_length=200, verbose_name="GitHub")
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, primary_key=True)
    curriculo = models.FileField(upload_to='curriculos/', verbose_name="Currículo em PDF")
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    usuario = models.ForeignKey(
        to=User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=False, 
        related_name="user")

    def __str__(self):
        return self.usuario.first_name

class Sobre(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    paragrafos = ArrayField(models.TextField(), blank=True)

class Empresa(models.Model):
    PORTE = [
        ("MEI", "Microempreendedor Individual"),
        ("ME", "Microempresa"),
        ("EPP", "Empresa de Pequeno Porte"),
        ("EMP", "Empresa de Médio Porte"),
        ("GP", "Grande Empresa")
    ]

    cnpj = models.CharField(max_length=18, null=False, blank=False)
    razao_social = models.CharField(max_length=100, null=False, blank=False)
    nome_fantasia = models.CharField(max_length=100, null=False, blank=False)
    porte = models.CharField(max_length=30, choices=PORTE, null=False, blank=False)
    site = models.URLField(max_length=200)
    email = models.EmailField(max_length=100)
    linkedin = models.URLField(max_length=200, verbose_name="LinkedIn")
    instagram = models.URLField(max_length=200)
    logo = models.ImageField(upload_to="logos/%Y/%m/%d/", blank=True)
    banner = models.ImageField(upload_to="banners/%Y/%m/%d/", blank=True)
    sobre = models.ForeignKey(
        to=Sobre, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=False, 
        related_name="sobre")
    usuario = models.ForeignKey(
        to=User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=False, 
        related_name="user")
    
class Recrutador(models.Model):
    usuario = models.ForeignKey(
        to=User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=False, 
        related_name="user")
    empresa = models.ForeignKey(
        to=Empresa, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=False, 
        related_name="emepresa")
    
class Vaga(models.Model):
    SENIORIDADE = [
        ("ESTAGIARIO", "Estagiário"),
        ("TRAINEE", "Trainee"),
        ("JUNIOR", "Júnior"),
        ("PLENO", "Pleno"),
        ("SENIOR", "Sênior"),
        ("ESPECIALITA", "Especialista")
    ]

    MODALIDADE_TRABALHO = [
        ("PRESENCIAL", "Presencial"),
        ("REMOTO", "Remoto"),
        ("HIBRIDO", "Híbrido")
    ]

    MODALIDADE_COTRATACAO = [
        ("EFETIVO", "Efetico (CLT)"),
        ("APRENDIZ", "Aprendiz"),
        ("ESTAGIO", "Estágio"),
        ("PJ", "Pessoa Jurídica (PJ)"),
        ("TRAINEE", "Trainee"),
        ("TEMPORARIO", "Temporário"),
        ("FREELANCER", "Freelancer"),
        ("TERCEIRO", "Terceiro"),
        ("BANCO_TALENTOS", "Banco de talentos"),
        ("VOLUNTARIO", "Voluntário"),
        ("SOCIO", "Sócio"),
        ("SUMMER JOB", "Summer Job")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField()
    senioridade = models.CharField(max_length=15, choices=SENIORIDADE, null=False, blank=False)
    modalidade_trabalho = models.CharField(max_length=15, choices=MODALIDADE_TRABALHO, null=False, blank=False)
    modalidade_contratacao = models.CharField(max_length=15, choices=MODALIDADE_COTRATACAO, null=False, blank=False)
    responsabilidades_atribuicoes = ArrayField(models.TextField(max_length=255), blank=True)
    requisitos_qualificacoes = ArrayField(models.TextField(max_length=255), blank=True)
    exclusiva_pcd = models.BooleanField(default=False)
    empresa = models.ForeignKey(
        to=Empresa, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=False, 
        related_name="emepresa")
