import sys

# Create your views here.


from .invertedIndex.InvertedIndex import *
from treatmentFile.leituraPDF.readPDF import pdf_to_txt
from treatmentFile.models.models import Texto
from .controlador.Requisicoes import *
from .controlador.Respostas import *

index = InvertedIndex()


class insertText(Requisicao):
    queryset = Texto.objects.all()


    def post(self, request):
        try:
            title = str(request.data['file'])
            texto = pdf_to_txt(request.data['file'])
            print(texto)
            print("\tstep 0")
            index.insert(texto,title,request.data['file'])
            return Response({'Status': True, 'Texto Adicionada': title})

        except Exception:
            return Response(
                {'Status': False, 'Texto Adicionada': title, 'Except': "Texto já foi inserido anteriomente",'Erro':str(sys.exc_info()[1])})
        except:
            return Response({'Status': False, 'Texto Adicionada': title})


class search(Requisicao):

    def get(self, request):
        try:
            search = request.data["search"]
            if search.find(" ") > 0:
                print("multisearch")
                group, relevance = index.multisearch(search)
                return Response({'Status': True, 'group': group, "relevance": relevance})
            else:
                print("search")
                relevance = index.search(search)
                return Response({'Status': True, 'group': 'No multiSearch', "relevance": relevance})
            return Respostas({"Status":"Algo do além está fazendo interferencias"})
        except:
            return Response({'Status': False, 'Search': search,'Erro':str(sys.exc_info()[1])})