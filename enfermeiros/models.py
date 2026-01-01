from django.db import models

# Create your models here.
from django.db import models


class Enfermeiro(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Ignorado'),
    ]

    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'),
        ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
    ]

    # Identificação SUS
    cns = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Cartão Nacional de Saúde (CNS)"
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF"
    )

    # Dados pessoais
    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    # Registro profissional (Enfermagem)
    coren = models.CharField(
        max_length=20,
        verbose_name="COREN"
    )

    coren_uf = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        verbose_name="UF do COREN"
    )

    cbo = models.CharField(
        max_length=6,
        verbose_name="Código Brasileiro de Ocupações (CBO)"
    )

    # Categoria profissional
    CATEGORIA_CHOICES = [
        ('ENF', 'Enfermeiro'),
        ('TEC', 'Técnico de Enfermagem'),
        ('AUX', 'Auxiliar de Enfermagem'),
    ]

    categoria = models.CharField(
        max_length=3,
        choices=CATEGORIA_CHOICES,
        verbose_name="Categoria Profissional"
    )

    # Contato
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # Vínculo institucional
    cnes = models.CharField(
        max_length=7,
        verbose_name="CNES do Estabelecimento"
    )

    # Controle
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome_completo} - COREN {self.coren}/{self.coren_uf}"
