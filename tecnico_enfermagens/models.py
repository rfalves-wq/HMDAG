from django.db import models


class TecnicoEnfermagem(models.Model):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Ignorado'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viúvo(a)'),
        ('U', 'União Estável'),
        ('I', 'Ignorado'),
    ]

    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'),
        ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'),
        ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
    ]

    # =====================
    # Identificação
    # =====================
    nome_completo = models.CharField(max_length=150)
    nome_social = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    cns = models.CharField("CNS", max_length=15, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)

    nome_mae = models.CharField(max_length=150)
    nome_pai = models.CharField(max_length=150, blank=True, null=True)

    # =====================
    # Contato
    # =====================
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    # =====================
    # Endereço
    # =====================
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)

    # =====================
    # Dados Profissionais
    # =====================
    coren = models.CharField(
        "COREN",
        max_length=20,
        help_text="Número do COREN do Técnico de Enfermagem"
    )
    coren_uf = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        verbose_name="UF do COREN"
    )

    ativo = models.BooleanField(default=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Técnico de Enfermagem"
        verbose_name_plural = "Técnicos de Enfermagem"
        ordering = ['nome_completo']

    def __str__(self):
        return self.nome_completo
