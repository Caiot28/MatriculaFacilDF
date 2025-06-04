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
    creche = models.ForeignKey(Creche, on_delete=models.CASCADE)
    nome_crianca = models.CharField(max_length=100)
    #data_nascimento = models.DateField()
    nome_responsavel = models.CharField(max_length=100)
    #cpf_responsavel = models.CharField(max_length=14)
    documento = models.FileField(upload_to='documentos/')
    data_matricula = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Matrícula {self.id} - {self.nome_crianca}"