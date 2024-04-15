from django.db import models

# Create your models here.

class CadastroDB(models.Model):
    nome = models.CharField(max_length=50)
    datadenascimento = models.DateField(max_length=50)
    email = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    mensagem = "Usuário cadastrado com sucesso!"