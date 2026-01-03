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
        ('SP', 'São Paulo'), ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    # Identificação SUS
    cns = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='CNS (Cartão Nacional de Saúde)'
    )

    cpf = models.CharField(
        max_length=11,
        unique=True
    )

    nome_completo = models.CharField(max_length=150)
    nome_social = models.CharField(max_length=150, blank=True, null=True)

    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    # Filiação (CadSUS)
    nome_mae = models.CharField(max_length=150)
    nome_pai = models.CharField(max_length=150, blank=True, null=True)

    # Contato
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    # Endereço
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)

    # Dados Profissionais (CNES)
    coren = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='COREN'
    )

    uf_coren = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        verbose_name='UF do COREN'
    )

    estabelecimento_cnes = models.CharField(
        max_length=7,
        verbose_name='CNES do Estabelecimento'
    )

    ativo = models.BooleanField(default=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Enfermeiro'
        verbose_name_plural = 'Enfermeiros'
        ordering = ['nome_completo']

    def __str__(self):
        return f'{self.nome_completo} - COREN {self.coren}'
