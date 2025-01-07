from django.db import models
import secrets


class Convidados(models.Model):
    STATUS_CHOICES = (
        ('AC', 'Aguardando confirmação'),
        ('C', 'Confirmado'),
        ('R', 'Recusado')
    )

    nome_convidado = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=25, null=True, blank=True)
    maximo_acompanhantes = models.PositiveIntegerField(default=0)
    token = models.CharField(max_length=25, blank=True)  
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AC')

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(16)  
        super(Convidados, self).save(*args, **kwargs)

    @property
    def link_convinte(self):
        return f'http://127.0.0.1:8000/convidados/?token={self.token}'

    def __str__(self):
        return f"{self.nome_convidado} (Status: {self.get_status_display()})"


class Presentes(models.Model):
    nome_presente = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='presentes')
    preco = models.DecimalField(max_digits=6, decimal_places=2)  
    importancia = models.IntegerField()
    reservado = models.BooleanField(default=False)
    reservado_por = models.ForeignKey(
        Convidados, null=True, blank=True, on_delete=models.DO_NOTHING,
        related_name="presentes_reservados"
    )

    def __str__(self):
        reservado_status = f"Reservado por {self.reservado_por}" if self.reservado else "Disponível"
        return f"{self.nome_presente} ({reservado_status})"

