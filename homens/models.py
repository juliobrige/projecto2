from django.db import models

# Create your models here.
class Presentes(models.Model):
    nome_presente = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='presentes')
    preco = models.DecimalField(max_digits=6, decimal_places=2)  
    importancia = models.IntegerField()
    reservado = models.BooleanField(default=False)  

    def __str__(self):
        return self.nome_presente
