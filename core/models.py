from django.db import models

# Create your models here.


class Stand(models.Model):
    location = models.CharField(max_length=100)
    price = models.FloatField()
    artista = models.CharField(max_length=100, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.location


class Reserva(models.Model):
    class Meta:
        ordering = ['date']

    cnpj = models.CharField(max_length=18)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quitado = models.BooleanField()
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
