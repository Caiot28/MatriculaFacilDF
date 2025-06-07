from django.db import models
from django.utils import timezone

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

"""class Matricula(models.Model):
    creche = models.ForeignKey(Creche, on_delete=models.CASCADE)
    nome_crianca = models.CharField(max_length=100)
    #data_nascimento = models.DateField()
    nome_responsavel = models.CharField(max_length=100)
    #cpf_responsavel = models.CharField(max_length=14)
    documento = models.FileField(upload_to='documentos/')
    data_matricula = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Matrícula {self.id} - {self.nome_crianca}"
        """
class Matricula(models.Model):
    # Relação com a creche
    creche = models.ForeignKey('Creche', on_delete=models.CASCADE)

    # Dados da criança
    nome_crianca = models.CharField(max_length=100)  # sem default
    data_nascimento = models.DateField(default='2000-01-01')
    sexo = models.CharField(
        max_length=20,
        choices=[
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
        ],
        default='Feminino'
    )

    # Dados do responsável
    nome_responsavel = models.CharField(max_length=100)  # sem default
    cpf_responsavel = models.CharField(max_length=14, default='000.000.000-00')
    telefone = models.CharField(max_length=20, default='(00)00000-0000')
    email = models.EmailField(default='email@exemplo.com')

    # Endereço normalizado
    endereco_rua = models.CharField(max_length=200, default='Rua Exemplo')
    endereco_numero = models.CharField(max_length=10, default='0')
    endereco_bairro = models.CharField(max_length=100, default='Bairro Exemplo')
    endereco_cidade = models.CharField(max_length=100, default='Cidade Exemplo')
    endereco_uf = models.CharField(max_length=2, default='DF')

    # Documentos (uploads)
    certidao_nascimento = models.FileField(upload_to='documentos/certidoes/', default='documentos/certidao_padrao.pdf')
    documento_responsavel = models.FileField(upload_to='documentos/documentos_responsavel/', default='documentos/documentos_responsavel_P.pdf')
    comprovante_residencia = models.FileField(upload_to='documentos/comprovantes_residencia/', default='comprovantes_residencia_P.pdf')

    # Data da matrícula (timestamp)
    data_matricula = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Matrícula {self.id} - {self.nome_crianca}"

