from django.urls import path
from .views import *

urlpatterns = [
    path('uploadFile', insertText.as_view(), name='uploadFile'),
    path('search/<str:search>',search.as_view(),name='search'),
    path('texto/<int:idtexto>',texto.as_view(),name='getTexto'),
    path('file/',file.as_view(),name='getFile')

]