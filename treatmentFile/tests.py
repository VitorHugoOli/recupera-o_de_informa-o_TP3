from django.test import TestCase

# Create your tests here.
from rest_framework.response import Response

from treatmentFile.controlador.Requisicoes import Requisicao
from treatmentFile.leituraPDF.readPDF import leituraPDF
from treatmentFile.models.models import Texto


class teste(Requisicao):

    def post(self, request):
        try:
            title = str(request.data['file'])
            texto = leituraPDF(request.data['file'])
            index.insert(texto,title)
            Texto.objects.create(titulo=title, texto=texto)
            Response({'Status': True, 'Texto Adicionada': title})
        except Exception:
            return Response(
                {'Status': False, 'Texto Adicionada': title, 'Except': "Texto já foi inserido anteriomente",'Erro':str(sys.exc_info()[1])})
        except:
            return Response({'Status': False, 'Texto Adicionada': title})