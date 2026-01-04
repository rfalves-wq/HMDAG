from django.db import models

# Create your models here.
from django.db import models


class Medico(models.Model):
    # -----------------------------
    # IDENTIFICAÇÃO
    # -----------------------------
    cns = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="CNS",
        help_text="Cartão Nacional de Saúde"
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF"
    )

    nome_completo = models.CharField(
        max_length=255,
        verbose_name="Nome completo"
    )

    nome_social = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Nome social"
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento"
    )

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Ignorado'),
    ]

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        verbose_name="Sexo"
    )

    # -----------------------------
    # DADOS PROFISSIONAIS
    # -----------------------------
    crm = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="CRM"
    )

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

    uf_crm = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        verbose_name="UF do CRM"
    )

    especialidade = models.CharField(
        max_length=255,
        verbose_name="Especialidade"
    )

    # -----------------------------
    # CONTATO
    # -----------------------------
    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Telefone"
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="E-mail"
    )

    # -----------------------------
    # ENDEREÇO
    # -----------------------------
    cep = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        verbose_name="CEP"
    )

    logradouro = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Logradouro"
    )

    numero = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Número"
    )

    complemento = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Complemento"
    )

    bairro = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Bairro"
    )

    municipio = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Município"
    )

    uf = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        blank=True,
        null=True,
        verbose_name="UF"
    )

    # -----------------------------
    # CONTROLE
    # -----------------------------
    ativo = models.BooleanField(
        default=True,
        verbose_name="Ativo no SUS"
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        ordering = ['nome_completo']

    def __str__(self):
        return f"{self.nome_completo} - CRM {self.crm}/{self.uf_crm}"
