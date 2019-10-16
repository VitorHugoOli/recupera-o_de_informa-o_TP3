from django.shortcuts import render

# Create your views here.
from treatmentFile.leituraPDF.readPDF import leituraPDF
from treatmentFile.models import Texto
from .controlador.Requisicoes import *
from .controlador.Respostas import *



class LerPDF(Requisicao):
    queryset = Texto.objects.all()

    def post(self, request):
        title = str(request.data['file'])
        print("\n\nTitulo: " + title)
        texto = leituraPDF(request.data['file'])
        print("\nTexto: \n" + texto)
        Texto.objects.create(titulo=title,
                             texto=texto)
        return Response({'Opa':'Deu BOM'})

    def get(self, request):
        arquivos = Texto.objects.filter()
        for i in arquivos:
            title = i.titulo
            texto = i.texto
        return Response({'titulo':title,'texto':texto})




