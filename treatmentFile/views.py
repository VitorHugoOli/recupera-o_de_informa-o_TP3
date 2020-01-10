import sys

# Create your views here.
from django.core.files.storage import FileSystemStorage

from .invertedIndex.InvertedIndex import *
from treatmentFile.leituraPDF.readPDF import pdf_to_txt
from treatmentFile.models.models import Texto
from .controlador.Requisicoes import *
from .controlador.Respostas import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import  *


index = InvertedIndex()


class insertText(Requisicao):
    def post(self, request):
        try:
            title = str(request.data['file'])
            texto = pdf_to_txt(request.data['file'])
            print(texto)
            print("\tstep 0")
            if index.insert(texto,title):
                return Response({'Status': True, 'Texto Adicionada': title})
            else:
                return Response(
                    {'Status': False, 'Texto Adicionada': title, 'Except': "Texto já foi inserido anteriomente"})
        except Exception:
            return Response(
                {'Status': False, 'Texto Adicionada': title, 'Erro':str(sys.exc_info()[1])})
        except:
            return Response({'Status': False, 'Texto Adicionada': title})


class search(Requisicao):
    def get(self, request,search):
        try:
            search = search
            # if search.find(" ") > 0:
            print("multisearch")
            group, relevance = index.multisearch(search)
            return Response({'Status': True, 'group': group, "relevance": relevance})
            # else:
            #     print("search")
            #     print(search)
            #     relevance = index.search(search)
            #     return Response({'Status': True, 'group': 'No multiSearch', "relevance": relevance})
            # return Respostas({"Status":"Algo do além está fazendo interferencias"})
        except:
            return Response({'Status': False, 'Search': search,'Erro':str(sys.exc_info()[1])})

class texto(Requisicao):
    def get(self, request,idtexto):
        try:
            id = idtexto
            texto = Texto.objects.get(id=id)
            return Response({'Status': True, 'Titulo': texto.titulo, 'Texto':texto.texto})

        except Exception:
            return Response(
                {'Status': False, 'Erro':str(sys.exc_info()[1])})


class file(Requisicao):
    def post(self, request):
        try:
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return Response({'Status': True, 'Titulo': uploaded_file_url})

        except Exception:
            return Response(

                {'Status': False, 'Erro':str(sys.exc_info()[1])})

