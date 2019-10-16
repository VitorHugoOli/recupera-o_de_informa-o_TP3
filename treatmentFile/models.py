from djongo import models


# Create your models here.
class Texto(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.CharField(max_length=1000000)

    def __str__(self):
        return self.titulo
