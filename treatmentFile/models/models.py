from django.contrib.postgres.fields import ArrayField
from djongo import models


# Create your models here.
class Texto(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.CharField(max_length=1000000)
    docfile = models.FileField(upload_to='documents')

    def __str__(self):
        return self.titulo

class indexInv(models.Model):
    word = models.CharField(max_length=45)


class DictWord(models.Model):
    indexInv = models.ForeignKey(indexInv,on_delete=models.CASCADE)
    idTexto = models.IntegerField()
    repeticoes = models.IntegerField()