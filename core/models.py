from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField() # O paramentro vazio indica preenchimento obrigatório
    data_criacao = models.DateTimeField(auto_now=True) # Parametro indicando preenchimento automático de data atual

    class Meta:
        db_table = 'evento' # Pré-define o nome da tabela criado

    def __str__(self):
        return self.titulo

