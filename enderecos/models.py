from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=150, null=True, blank=True)
    linha2 = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    lat = models.IntegerField(null=True, blank=True)
    lng = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
