from django.db import models

class RegiaoAdministrativa(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Creche(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.TextField()
    regiao = models.ForeignKey(RegiaoAdministrativa, on_delete=models.CASCADE)
    vagas_disponiveis = models.PositiveIntegerField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nome} - {self.regiao.nome}"

class Matricula(models.Model):
    
    STATUS_CHOICES = [
        ('analise', 'Em análise'),
        ('aprovada', 'Aprovada'),
        ('recusada', 'Recusada'),
    ]
    
    creche = models.ForeignKey('Creche', on_delete=models.CASCADE)

    # Dados da criança
    nome_crianca = models.CharField(max_length=100)  # sem default
    data_nascimento = models.DateField()
    sexo = models.CharField(
        max_length=20,
        choices=[
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
        ]
    )

    # Dados do responsável
    nome_responsavel = models.CharField(max_length=100)
    cpf_responsavel = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    endereco_rua = models.CharField(max_length=200)
    endereco_numero = models.CharField(max_length=10)
    endereco_bairro = models.CharField(max_length=100)
    endereco_cidade = models.CharField(max_length=100)
    endereco_uf = models.CharField(max_length=2)

    # Documentos (uploads)
    certidao_nascimento = models.FileField(upload_to='documentos/certidoes/')
    documento_responsavel = models.FileField(upload_to='documentos/documentos_responsavel/')
    comprovante_residencia = models.FileField(upload_to='documentos/comprovantes_residencia/')
    
     # Status da matrícula
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='analise')
    motivo_recusa = models.TextField(blank=True, null=True)

    # Data da matrícula
    data_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Matrícula {self.id} - {self.nome_crianca}"

