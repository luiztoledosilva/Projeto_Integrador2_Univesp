from django.db import models

class Receita(models.model):
    nome = models.CharField(max_length=20, db_index=True)
    descricao = models.CharField(max_length=500)


    def __str__(self):
        #return super().__str__()
        return self.nome